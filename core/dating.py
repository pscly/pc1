import pyautogui
import time

def xuan_yx():
    """
    选英雄
    """

    
    # 开始选择英雄
    if x := pyautogui.locateOnScreen('img/yx/vn.png', grayscale=True):
        pyautogui.click(x)
    elif x := pyautogui.locateOnScreen('img/yx/jks.png', grayscale=True):
        pyautogui.click(x)
    elif x := pyautogui.locateOnScreen('img/yx/sn.png', grayscale=True):
        pyautogui.click(x)
        
    # 确定英雄
    if x:= pyautogui.locateOnScreen('img/ok2.png'):
        pyautogui.click(x)
    time.sleep(1)
    
if __name__ == '__main__':
    xuan_yx()