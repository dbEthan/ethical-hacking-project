# Source used: https://pyshark.com/take-screenshot-using-python/
import os
import pyautogui

def run(**args):
    print("[*] Taking screenshot.")
    size = pyautogui.size()
    screenshot = pyautogui.screenshot(region=(size.width, size.height))
    screenshot.save("screenshot.jpg")
    
    with open("screenshot.jpg", "rb") as f:
        image_bytes = f.read()
    
    os.remove("screenshot.jpg")
    
    return image_bytes
