from PIL import ImageGrab

def take_screenshot():
    path = 'screenshot.jpg'
    screenshot = ImageGrab.grab() # this will have the raw data
    rgb_screenshot = screenshot.convert('RGB') #raw data gets converted to RGB
    rgb_screenshot.save(path, quality = 15)

take_screenshot()