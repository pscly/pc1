# 控制windows 计算机的键盘鼠标
# 打开steam
import re
import sys
# 将上个目录添加到环境变量
sys.path.append('..')


import pyautogui
import time
import random
import win32api
import win32con
import win32gui
import pyautogui
from ctypes import windll
from xn_key import press, press_down, press_up, press_down_t
from core import all1

云顶点击1 = (1920/2, 1080/2)

def shopping():
    """
    现在的购买就只是打开一下购买界面然后关闭，让系统自己买
    """
    
    press('p')
            
    # 判断购买装备有没有
    if x := pyautogui.locateOnScreen('img/game/gm_sy.png', grayscale=True):
        pyautogui.click(x)
        pyautogui.doubleClick(x)
        pyautogui.doubleClick(x)
        print('买了总体不错')
    # elif x := pyautogui.locateOnScreen('img/game/shop/lydk.png', grayscale=True):
    #     pyautogui.click(x)
    #     # 点击购买
    #     print('购买装备')
    #     pyautogui.doubleClick(x)
    #     pyautogui.doubleClick(x)
    #     print('买了利于对抗')
    press('p')
    print('买完了')

def play_game():
    m = 0   # 购买商店的东西
    over = 0
    shopping()
    
    while 1:
        if not win32gui.FindWindow(None, 'League of Legends (TM) Client'):
            print('游戏结束')
            return "游戏结束"
        # 如果鼠标在屏幕四角
        if pyautogui.position()[0] < 10 or pyautogui.position()[1] < 10 or pyautogui.position()[0] > 1920 or pyautogui.position()[1] > 1080:
            raise Exception('鼠标在屏幕四角, 程序强行退出')
            
        m += 1
        time.sleep(1)
        # move_up(n)
        print('--正在打L--')
        # 输入 a 键
        # 移动鼠标到(1244, 281)
        pyautogui.moveTo(1344, 118, duration=0.1)
        press_down('space')
        # 按 3 下a键
        press('a')
        press('a')
        press('1')  # 喝药 
        press('a')
        press('q')
        press('w')
        press('e')
        press('r')
        press('ctrl+q')
        press('ctrl+w')
        press('ctrl+e')
        press('a')
        press('a')
        press('a')
        press_up('space')
        
        if m > 60:   # 我打算后期改为 30 以上，避免太频繁
            print(f'购买为{m}')
            # 按下b键, 并且等待10秒
            press('b')
            print('打算购买装备,免得说我挂机')
            time.sleep(10)
            # 购买
            shopping()
            m = 0
            
            
        if over > 3:
            # 判断图片是否存在
            if x:= pyautogui.locateOnScreen('img/game/jx.png', grayscale=True):
                return '游戏结束'
            over = 0

def play_yunding():
    while 1:
        print('云顶ing')
        if not win32gui.FindWindow(None, 'League of Legends (TM) Client'):
            print('游戏结束')
            return "游戏结束"
        # 如果鼠标在屏幕四角
        if pyautogui.position()[0] < 10 or pyautogui.position()[1] < 10 or pyautogui.position()[0] > 1920 or pyautogui.position()[1] > 1080:
            raise Exception('鼠标在屏幕四角, 程序强行退出')
        if x := pyautogui.locateOnScreen('img/yd/exit.png', grayscale=True):
            # 使用句柄结束进程
            windll.user32.PostMessageA(win32gui.FindWindow(None, 'League of Legends (TM) Client'), win32con.WM_CLOSE, 0, 0)
            print('退出云顶了')

            if x := pyautogui.locateOnScreen('img/exit0.png', grayscale=True):
                pyautogui.click(x)
            return '退出云顶'
            # pyautogui.leftClick(x)
            # print('点击退出云顶')
            # time.sleep(3)
            

        # pyautogui.moveTo(云顶点击1)
        # pyautogui.rightClick(云顶点击1)
        # pyautogui.leftClick(云顶点击1)
        # pyautogui.leftClick(云顶点击1)
        pyautogui.leftClick((413,768))
        pyautogui.moveTo(587,991, duration=2)
        # 左键按住不放，拖动到(587,991)
        pyautogui.dragTo(587,991, duration=2)
        # pyautogui.click(clicks=2, interval=0.25)
        # pyautogui.leftClick((587,991))
        pyautogui.leftClick((587,991))

        # pyautogui.click(941,34, button='left')pyautogui.dragRel(0,100, button='left', duration=5) # 点击加向下拖动
        time.sleep(2)




if __name__ == '__main__':
    # win32gui.SetForegroundWindow(win32gui.FindWindow(None, 'League of Legends (TM) Client'))
    # play_game()
    play_yunding()

    