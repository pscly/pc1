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



VK_CODE = {'a':0x41, 'b':0x42, 'q': 0x51, 'w': 0x57, 'e': 0x45, 'r': 0x52, 'd': 0x44, 'f': 0x46, 'b': 0x42, 'p': 0x50, 'y': 0x59,
           'esc': 0x1B, 'F1': 0x70}



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

def key_press(vk_code):
    win32api.keybd_event(vk_code, 0, 0, 0)
    win32api.keybd_event(vk_code, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)



# 键盘输入
def input_key(key):
    pyautogui.typewrite(key, interval=0.1)
        
    
if __name__ == '__main__':
    m = 0   # 购买商店的东西
    ss = 0  # 避免多跑(浪费时间和性能)
    ks = 0  # 点击开始
    while 1:
        if pyautogui.position() == (0, 0):
            print('退出')
            break
        
        # 随机小数1-3
        if x := pyautogui.locateOnScreen('img/c1.png'):
            pyautogui.click(x)
        
        
        # 查看是否有图片，如果有就是在游戏里面
        elif pyautogui.locateOnScreen('img/b.png'):
            ss = 1
            m += 1
            n = get_random(30, 800)
            move_up(n)
            print('--正在打L--')
            print('')
            # 输入 a 键
            # 移动鼠标到(1244, 331)
            # pyautogui.moveTo(1244, 331, duration=0.1)
            # 按下鼠标右键
            pyautogui.click(button='right')
            key_press(VK_CODE['a'])
            move_down(n)
            
            if m > 1:   # 我打算后期改为 30 以上，避免太频繁
                # 按下b键, 并且等待10秒
                key_press(VK_CODE['b'])
                print('打算购买装备,免得说我挂机')
                time.sleep(10)
                # 购买
                key_press(VK_CODE['p'])
                # 购买推荐
                

            continue

        