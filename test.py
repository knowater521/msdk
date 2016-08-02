# -*- coding: utf-8 -*-
import time
#from ctypes import *

import ctypes
import platform

win_bit = platform.architecture()[0]
if win_bit == "64bit":
    api = ctypes.CDLL("win64/msdk.dll")

vid = api.M_Open(1)
api.M_ResetMousePos(vid)
time.sleep(1)
api.M_MoveTo(vid, 200, 200)
time.sleep(5)
api.M_LeftClick(vid, 2)
time.sleep(1)