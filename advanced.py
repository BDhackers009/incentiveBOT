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

def move_mouse_human_like(x, y):
    pyautogui.moveTo(x + random.randint(-5, 5), y + random.randint(-5, 5), duration=random.uniform(0.5, 1.5))

while True:
    if not is_running:
        time.sleep(1)
        continue

    image_path_incentive = "incentive2.png"
    location_incentive = pyautogui.locateOnScreen(image_path_incentive, confidence=random.uniform(0.75, 0.85))

    if location_incentive:
        print(f"incentive2.png found at: {location_incentive.left}, {location_incentive.top}")
        center_incentive = pyautogui.center(location_incentive)
        move_mouse_human_like(center_incentive.x, center_incentive.y)
        pyautogui.click()
        print(f"Clicked on incentive2.png at: {center_incentive.x}, {center_incentive.y}")
        time.sleep(random.uniform(15, 20))

        image_path_metamask = "metamask_processed.png"
        location_metamask = pyautogui.locateOnScreen(image_path_metamask, confidence=random.uniform(0.55, 0.65))

        if location_metamask:
            print(f"metamask_processed.png found at: {location_metamask.left}, {location_metamask.top}")
            center_metamask = pyautogui.center(location_metamask)
            move_mouse_human_like(center_metamask.x, center_metamask.y)
            pyautogui.click()
            print(f"Clicked on metamask_processed.png at: {center_metamask.x}, {center_metamask.y}")
            time.sleep(random.uniform(7, 10))
        else:
            print("metamask_processed.png not found on the screen.")
    else:
        print("incentive2.png not found on the screen.")