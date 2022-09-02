from PIL.Image import Image
import pyautogui
import time

from pyautogui import ImageNotFoundException
interval = 2
i=0
pyautogui.size()
while(i<10):
    try:
        pyautogui.click('redGC.png')
        time.sleep(.1)
        pyautogui.click('closeGC.png')
        time.sleep(.25)
        pyautogui.click('leaveGC.png')
        print("found")
        time.sleep(1)
    except Exception as e:
        print('red image not found')
        time.sleep(interval)
    try:
        pyautogui.click('orangeGC.png')
        time.sleep(.1)
        pyautogui.click('closeGC.png')
        time.sleep(.25)
        pyautogui.click('leaveGC.png')
        print("found")
        time.sleep(1)
    except Exception as e:
        print('orange image not found')
        time.sleep(interval)
    try:
        pyautogui.click('yellowGC.png')
        time.sleep(.1)
        pyautogui.click('closeGC.png')
        time.sleep(.25)
        pyautogui.click('leaveGC.png')
        print("found")
        time.sleep(1)
    except Exception as e:
        print('yellow image not found')
        time.sleep(interval)
    try:
        pyautogui.click('greenGC.png')
        time.sleep(.1)
        pyautogui.click('closeGC.png')
        time.sleep(.25)
        pyautogui.click('leaveGC.png')
        print("found")
        time.sleep(1)
    except Exception as e:
        print('green image not found')
        time.sleep(interval)
    try:
        pyautogui.click('blueGC.png')
        time.sleep(.1)
        pyautogui.click('closeGC.png')
        time.sleep(.25)
        pyautogui.click('leaveGC.png')
        print("found")
        time.sleep(1)
    except Exception as e:
        print('blue image not found')
    try:
        pyautogui.click('cyanGC.png')
        time.sleep(.1)
        pyautogui.click('closeGC.png')
        time.sleep(.25)
        pyautogui.click('leaveGC.png')
        print("found")
        time.sleep(1)
    except Exception as e:
        print('cyan image not found')
        time.sleep(interval)
    try:
        pyautogui.click('purpleGC.png')
        time.sleep(.1)
        pyautogui.click('closeGC.png')
        time.sleep(.25)
        pyautogui.click('leaveGC.png')
        print("found")
        time.sleep(1)
    except Exception as e:
        print('purple image not found')
        time.sleep(interval)
