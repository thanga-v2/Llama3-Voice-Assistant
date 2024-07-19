import os

from groq import Groq
from dotenv import load_dotenv

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


prompt = input('USER: ')
response = groq_prompt(prompt)

print(response)


