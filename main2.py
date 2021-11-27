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
from xn_key import press, press_down
from core import all1,dating, gameing




if __name__ == '__main__':
    m = 0   # 购买商店的东西
    ks = 0  # 点击开始
    while 1:
        # 如果鼠标在屏幕四角
        if pyautogui.position()[0] < 10 or pyautogui.position()[1] < 10 or pyautogui.position()[0] > 1920 or pyautogui.position()[1] > 1080:
            raise Exception('鼠标在屏幕四角, 程序强行退出')
            
        
        # 通过查看句柄，查看游戏是否存在
        if game_win := win32gui.FindWindow(None, 'League of Legends (TM) Client'):
            
            # 将窗口句柄打开
            win32gui.SetForegroundWindow(game_win)
            
            print('前往打游戏')
            # 跳转打游戏功能处
            time.sleep(1)
            gameing.play_game()
            time.sleep(3)
        
        
            # 再玩一次 
            if x := pyautogui.locateOnScreen('img/zailai.png'):
                # 到图片中心位置点击左键
                pyautogui.click(x)
                print('再玩一次')
                time.sleep(6)
                # 单机左键
                pyautogui.click(button='left')
        
        
        elif (x := pyautogui.locateOnScreen('img/zailai.png', grayscale=True)):
            pyautogui.click(x)
            print('点击再玩一次')
            
        elif x := pyautogui.locateOnScreen('img/start1.png'):
            # 到图片中心位置点击左键
            pyautogui.click(x)
            print('寻找对局')

            # 如果没有找到对局，就一直等待
            while 1:
                """这里是一直循环等待确认对局, """
                if x := pyautogui.locateOnScreen('img/jieshou1.png', grayscale=True):
                    pyautogui.click(x)
                    print('确认对局')

                if x := pyautogui.locateOnScreen('img/xz1.png', grayscale=True):
                    dating.xuan_yx()
                    print('英雄选择完毕')
                    # 选好了英雄就该跳出循环了
                    break
                        

        else:
            print('未匹配到任何')
            # 将光标移动到屏幕中心
            pyautogui.moveTo(1920/2, 1080/2)
            time.sleep(3)
        

        # 如果鼠标在0, 0 就强行退出
