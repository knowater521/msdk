# -*- coding: utf-8 -*-
import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

time.sleep(5)

def screenshot_single(imgage_name):
    pyautogui.hotkey('ctrl', 'shift', 's')
    pyautogui.typewrite(imgage_name)
    pyautogui.press('enter')

if __name__=='__main__':
    for i in range(15):
        pyautogui.hotkey('ctrl', 'shift', 's')
        pyautogui.typewrite(str(i))
        pyautogui.press('enter')