# 控制windows 计算机的键盘鼠标
# 打开steam

import pyautogui
import time
import random


# 获取n to n2 之间的随机数
def get_random(n, n2):
    return random.randint(n, n2)

# 向上移动鼠标 n px
def move_up(n):
    pyautogui.moveRel(0, -n, duration=0.1)

# 向下移动鼠标 n px
def move_down(n):
    pyautogui.moveRel(0, n, duration=0.1)
    
# 向左移动鼠标 n px
def move_left(n):
    pyautogui.moveRel(-n, 0, duration=0.1)
    
# 向右移动鼠标 n px
def move_right(n):
    pyautogui.moveRel(n, 0, duration=0.1)

# 单击鼠标左键
def click_left():
    pyautogui.click(button='left')
    


if __name__ == '__main__':
    b = 0
    
    while 1:
        n = get_random(30, 900)
        time_n = get_random(10, 30)
        move_left(n)
        print('------')
        time.sleep(time_n)
        print('--2---')
        move_right(n)

        # 如果鼠标在0, 0 就强行退出
        if pyautogui.position() == (0, 0):
            print('退出')
            break
        

