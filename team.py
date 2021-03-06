# ************ Requirement ************
# Python Version: 3.8
# Run below cmds install packages:
# * pip install pywin32
# * pip install pyautogui
# * pip install pyclick

import win32gui
import pyautogui
import sys
import random
import time
from pyclick import HumanClicker

pyautogui.FAILSAFE = False

print('Press Ctrl-C to quit.')

hc = HumanClicker()

# Each round will cost 45 seconds
waitingTime = 45

# Screen size
screenWidth, screenHeight = pyautogui.size()

# Generate start button position
def get_start_random_position(window):
    w = window[2] - window[0]
    h = window[3] - window[1]
    
    start_x = int(window[2] - w * 0.0811)
    start_y = int(window[3] - h * 0.1539)
    start_w = int(w * 0.05)
    start_h = int(h * 0.07)
    # -------------------- Debug ----------------------- #
    # print("\nStart location range:")
    # print("\t x: %d (max: %d)" % (start_x, (start_x + start_w)))
    # print("\t y: %d (max: %d)" % (start_y, (start_y + start_h)))
    # print("\t width: %d" % start_w)
    # print("\t height: %d" % start_h)
    # -------------------- Debug ----------------------- #
    
    position = []
    # -------------------- Debug ----------------------- #
    # position.append(start_x)
    # position.append(start_y)
    # -------------------- Debug ----------------------- #
    position.append(random.randint(start_x, start_x + start_w))
    position.append(random.randint(start_y, start_y + start_h))
    return position

# Generate close click position
def get_close_random_position(window):
    w = window[2] - window[0]
    h = window[3] - window[1]

    start_x = int(window[0] + w * 0.03)
    start_y = int(window[1] + h * 0.07)
    start_w = int(w * 0.45)
    start_h = int(h * 0.1)
    # -------------------- Debug ----------------------- #
    # print("\nStart location range:")
    # print("\t x: %d (max: %d)" % (start_x, (start_x + start_w)))
    # print("\t y: %d (max: %d)" % (start_y, (start_y + start_h)))
    # print("\t width: %d" % start_w)
    # print("\t height: %d" % start_h)
    # -------------------- Debug ----------------------- #

    position = []
    # -------------------- Debug ----------------------- #
    # position.append(start_x)
    # position.append(start_y)
    # -------------------- Debug ----------------------- #
    position.append(random.randint(start_x, start_x + start_w))
    position.append(random.randint(start_y, start_y + start_h))
    return position

# Search Onmyoji windows
# win32gui.EnumWindows callback exmaple:
# ******************************************************
#   rect = win32gui.GetWindowRect(hwnd)
#   x = rect[0]
#   y = rect[1]
#   w = rect[2] - x
#   h = rect[3] - y
#   print("Onmyoji Window %s:" % win32gui.GetWindowText(hwnd))
#   print("\tLocation: (%d, %d)" % (x, y))
#   print("\t    Size: (%d, %d)" % (w, h))
# ******************************************************
def search_onmyoji_windows():
    def callback(hwnd, extra):
        if win32gui.GetWindowText(hwnd)=="阴阳师-网易游戏":
            extra.append(win32gui.GetWindowRect(hwnd))
    
    windows = []
    win32gui.EnumWindows(callback, windows)
    return windows

# Search Onmyoji windows
windows = search_onmyoji_windows()

if (len(windows) != 2):
    print("Error: Team mode needs 2 Onmyoji.")

# Chose which one is the primary window
# Make window_1 as primary window as default
window_1 = windows[0]
window_2 = windows[1]

print("Onmyoji Window - 1")
print("Location: (%d, %d, %d, %d)" % (windows[0][0], windows[0][1], windows[0][2], windows[0][3]))

print("\nOnmyoji Window - 2")
print("Location: (%d, %d, %d, %d)" % (windows[1][0], windows[1][1], windows[1][2], windows[1][3]))

print("Please chose which one is the primary window(1 or 2):")
n = input()

if (n == "1"):
    print("Onmyoji Window - 1 is team leader.")
elif (n == "2"):
    # If '2' second is the primary window, swap window_1 and window_2
    window_1 = windows[1]
    window_2 = windows[0]
    print("Onmyoji Window - 2 is team leader.")
else:
    print("Invalid input.")

# -------------------- Start -------------------- #
index = 1
while 1:
    print("Round: %d" % index)

    # Move to start button then click
    start_position = get_start_random_position(window_1)
    startX = start_position[0]
    startY = start_position[1]

    # Start
    hc.move((startX, startY), 1)
    hc.click()

    # Move to a random location of screen
    hc.move((random.randint(0, screenWidth), random.randint(0, screenHeight)), 1)

    # Waiting until finish
    time.sleep(waitingTime)

     # Close capation rewards page
    windows_1_close_position = get_close_random_position(window_1)
    hc.move((windows_1_close_position[0], windows_1_close_position[1]), 1)
    hc.click()

     # Close teammate rewards page
    windows_2_close_position = get_close_random_position(window_2)
    hc.move((windows_2_close_position[0], windows_2_close_position[1]), 1)
    hc.click()

    index = index + 1