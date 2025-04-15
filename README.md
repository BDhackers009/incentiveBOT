# incentiveBOT

This repository contains Python scripts for automating tasks using PyAutoGUI. The scripts are designed to locate and interact with specific images on the screen, simulating human-like behavior to avoid detection.

## Features
- Detect and click on specific images (e.g., `incentive2.png` and `metamask.png`).
- Randomized mouse movements and delays to mimic human actions.
- Hotkey support to play/pause the script.
- Image preprocessing for better recognition.

## Prerequisites
1. Python 3.x installed on your system.
2. Install the required Python libraries:
   ```bash
   pip install pyautogui opencv-python pillow keyboard
   ```
3. Ensure the images (`incentive2.png`, `metamask.png`) are in the same directory as the scripts.

## Files

- `automate.py`: Automates clicking on `incentive2.png` and `metamask.png` with basic functionality.
- `advanced.py`: An advanced version of the automation script with human-like behavior and dynamic confidence levels.

## Usage

### Running the Scripts
0. Open incentive.finance and go to trade and set trade % then run the script as follows.

2. Run the automation script:
   ```python
   python advanced.py
   ```
   or
   ```python
   python automate.py
   ```

3. Press `P` to play/pause the script while it is running.

### 
- Video tutorial:-

[![YouTube](http://i.ytimg.com/vi/r9wDaPkGefk/hqdefault.jpg)](https://www.youtube.com/watch?v=r9wDaPkGefk)
  
### Notes
- Ensure the screen resolution and scaling match the images for accurate detection.
- Adjust the confidence levels in the scripts if the images are not being detected properly.

## Author
Created by [bdhackers009](https://github.com/bdhackers009).
