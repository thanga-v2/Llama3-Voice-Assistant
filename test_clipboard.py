import pyperclip

def get_clipboard_text():
    clipboard_content = pyperclip.paste()
    if isinstance(clipboard_content, str):
        return clipboard_content
    else:
        print("Nothing to copy from the clip board")
        return None


print(get_clipboard_text())