
import pyautogui
import time
import random
import win32api
import win32con
import win32gui
import pyautogui
from ctypes import windll
from xn_key import press, press_down


# 获取n to n2 之间的随机数
def get_random(n, n2):
    return random.randint(n, n2)

# 向上移动鼠标 n px
def move_up(n):
    pyautogui.moveRel(0, -n, duration=0.1)

# 向下移动鼠标 n px
def move_down(n):
    pyautogui.moveRel(0, n, duration=0.1)

# 单击鼠标左键
def click_left():
    pyautogui.click(button='left')
    
# 单击鼠标右键
def click_right():
    pyautogui.click(button='right')

# 键盘输入
def input_key(key):
    '''
    这个是低级的键盘输入
    '''
    pyautogui.typewrite(key, interval=0.1)


    