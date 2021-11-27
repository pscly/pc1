
# 控制windows 计算机的键盘鼠标
# 打开steam

import pyautogui
import time
import random
import win32api
import win32con
import win32gui
import pyautogui
from ctypes import windll
from v_keys import VK_CODE




# 键盘输入
def key_press(k):
    k = k.lower()
    if k not in VK_CODE:
        raise ValueError('键盘键值错误')
    vk_code = VK_CODE[k]
    win32api.keybd_event(vk_code, 0, 0, 0)
    win32api.keybd_event(vk_code, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)
    
if __name__ == '__main__':
    time.sleep(5)
    key_press('a')
    