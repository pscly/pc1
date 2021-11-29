# 控制windows 计算机的键盘鼠标
# 打开steam
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
from pen import pen2


def shuohua(s):
    # 按下回车
    press('enter')
    # 键盘输入文字
    pyautogui.typewrite(s, interval=0.1)
    press('enter')
    
def ma():
    p = pen2.Pen()
    shuohua(p.start())
    # shuohua('asdf')

def shopping():
    """
    现在的购买就只是打开一下购买界面然后关闭，让系统自己买
    """
    
    press('p')
            
    press('p')
    print('买完了')

def play_game():
    over = 0
    
    while 1:
        if not win32gui.FindWindow(None, 'League of Legends (TM) Client'):
            print('游戏结束')
            return "游戏结束"
        # 如果鼠标在屏幕四角
        if pyautogui.position()[0] < 10 or pyautogui.position()[1] < 10 or pyautogui.position()[0] > 1920 or pyautogui.position()[1] > 1080:
            raise Exception('鼠标在屏幕四角, 程序强行退出')

        # 如果挂机提醒
        if x := pyautogui.locateOnScreen('img/game/ok.png'):
            pyautogui.click(x)
            
        time.sleep(1)
        # move_up(n)
        print('--正在打L--')
        # 输入 a 键
        # 移动鼠标到(1244, 281)
        press_down('space')
        pyautogui.moveTo(1344, 118, duration=0.1)
        # 鼠标向上移动 50 px
        pyautogui.moveRel(0, -50, duration=0.1)
        # 鼠标向下移动 50 px
        pyautogui.moveRel(0, 50, duration=0.1)
        # 按 3 下a键
        press_up('space')
            
        if over > 3:
            # 判断图片是否存在
            if x:= pyautogui.locateOnScreen('img/game/jx.png', grayscale=True):
                return '游戏结束'
            over = 0
    

if __name__ == '__main__':
    # win32gui.SetForegroundWindow(win32gui.FindWindow(None, 'League of Legends (TM) Client'))
    # play_game()
    ma()
    
    