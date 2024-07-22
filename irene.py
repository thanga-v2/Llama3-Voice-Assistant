import os

from groq import Groq
from dotenv import load_dotenv
# need to take the imagegrab class from PIL (for screenshots)
from PIL import ImageGrab
import cv2
import pyperclip


webcam = cv2.VideoCapture(0)

load_dotenv()

# Groq_key = os.getenv('GROQ_KEY')
# print(Groq_key)
groq_cli = Groq(api_key=os.getenv('GROQ_KEY'))

def groq_prompt(prompt):
    convo = [{'role': 'user', 'content': prompt}]
    #calling the groq client to create a response by passing the convo list we created above
    chat_completion = groq_cli.chat.completions.create(messages=convo, model='llama3-70b-8192')
    response = chat_completion.choices[0].message

    return response.content

#
# BELOW IS THE FUNCTION TO CALL FUNCTIONS IN THE LANGUAGE MODEL
#

def function_call(prompt):
    sys_msg = (
        'You are an AI function calling model. You will determine whether extracting the users clipboard content, '
        'taking a screenshot, capturing the webcam or calling no functions is best for a voice assistant to respond'
        'to the users prompt. The webcam can be assumed to be a normal laptop webcam facing the user. You will '
        'respond with only one selection from the list: ["extract clipboard", "take screenshot", "capture webcam", "None"] \n'
        'Do not respond with anything but the most logical selection from that list with no explanations. Format the'
        'function call name exactly as I listed.'
    )

    function_convo = [
        {
            'role':'system', 'content': sys_msg
        },
        {
            'role':'user', 'content':prompt
        }
    ]

    chat_completion = groq_cli.chat.completions.create(messages=function_convo, model='llama3-70b-8192')
    response = chat_completion.choices[0].message

    return response.content
def take_screenshot():
    path = 'screenshot.jpg'
    screenshot = ImageGrab.grab() # this will have the raw data
    rgb_screenshot = screenshot.convert('RGB') #raw data gets converted to RGB
    rgb_screenshot.save(path, quality = 15)

def webcam_capture():
    if not webcam.isOpened():
        print('Error: Not Successfully opened. Exit')
        exit()

    else:
        print("Stay still,, Say cheese !")

    path='webcam.jpg'
    ret, frame = webcam.read()
    cv2.imwrite(path, frame)


def get_clipboard_text():
    clipboard_content = pyperclip.paste()
    if isinstance(clipboard_content, str):
        return clipboard_content
    else:
        print("Nothing to copy from the clip board")
        return None


# print(get_clipboard_text())


prompt = input('USER: ')
#
# below should send the prompt response to our function - function_call
#
function_response = function_call(prompt)
print(f'Function response : {function_response}')
response = groq_prompt(prompt)

print(response)


