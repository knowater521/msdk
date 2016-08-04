# -*- coding: utf-8 -*-
import time
#from ctypes import *
import sys
import ctypes
import platform
from auto_screenshoot import screenshot_single
win_bit = platform.architecture()[0]
print win_bit

if win_bit == "64bit":
    api = ctypes.CDLL("win64/msdk.dll")
else:
    print "32"
    api = ctypes.windll.LoadLibrary("win32/msdk.dll")

#api = ctypes.cdll.LoadLibrary("win32/msdk.dll")

#api = ctypes.CDLL("win32/msdk.dll")

#api = ctypes.windll.LoadLibrary("win32/msdk.dll")

#api = ctypes.WinDLL("win32/msdk.dll")


vid = api.M_Open(1)
#vid = api.M_Open(int_id)
api.M_ResetMousePos(vid)
time.sleep(2)
api.M_MoveTo(vid,340, 1050)
time.sleep(5)


for i in range(2):
    screenshot_single(str(i))
    api.M_LeftClick(vid, 1)
    time.sleep(3)
    print i
