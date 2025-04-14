import pyautogui
import time
import random
import keyboard

time.sleep(5)
is_running = True

def toggle_running():
    global is_running
    is_running = not is_running
    state = "Running" if is_running else "Paused"
    print(f"Script is now {state}.")

keyboard.add_hotkey("p", toggle_running)

print("Press P to play/pause the script.")

while True:
    if not is_running:
        time.sleep(1)
        continue

    image_path_incentive = "incentive2.png"
    location_incentive = pyautogui.locateOnScreen(image_path_incentive, confidence=0.8)

    if location_incentive:
        print(f"incentive2.png found at: {location_incentive.left}, {location_incentive.top}")
        center_incentive = pyautogui.center(location_incentive)
        pyautogui.moveTo(center_incentive.x, center_incentive.y)
        pyautogui.click()
        print(f"Clicked on incentive2.png at: {center_incentive.x}, {center_incentive.y}")
        wait_time = random.randint(15, 20)
        print(f"Waiting for {wait_time} seconds...")
        time.sleep(wait_time)

        image_path_metamask = "metamask.png"
        location_metamask = pyautogui.locateOnScreen(image_path_metamask, confidence=0.6)

        if location_metamask:
            print(f"metamask.png found at: {location_metamask.left}, {location_metamask.top}")
            center_metamask = pyautogui.center(location_metamask)
            pyautogui.moveTo(center_metamask.x, center_metamask.y)
            pyautogui.click()
            print(f"Clicked on metamask.png at: {center_metamask.x}, {center_metamask.y}")
            wait_time = random.randint(7, 10)
            print(f"Waiting for {wait_time} seconds...")
            time.sleep(wait_time)
        else:
            print("metamask.png not found on the screen.")
    else:
        print("incentive2.png not found on the screen.")