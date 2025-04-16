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

def find_and_click(image_path, confidence, retries=3):
    for attempt in range(retries):
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            print(f"{image_path} found at: {location.left}, {location.top}")
            center = pyautogui.center(location)
            pyautogui.moveTo(center.x, center.y)
            pyautogui.click()
            print(f"Clicked on {image_path} at: {center.x}, {center.y}")
            return True
        else:
            print(f"Attempt {attempt + 1} to find {image_path} failed. Retrying...")
            time.sleep(1)
    print(f"{image_path} not found after {retries} attempts.")
    return False

while True:
    if not is_running:
        time.sleep(1)
        continue

    if find_and_click("incentive2.png", confidence=0.8):
        wait_time = random.randint(15, 20)
        print(f"Waiting for {wait_time} seconds...")
        time.sleep(wait_time)
        find_and_click("metamask_processed.png", confidence=0.6)