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
    pyautogui.click(pyautogui.locateOnScreen('img/yx/ok1.png', grayscale=True))
    time.sleep(20)
    
if __name__ == '__main__':
    xuan_yx()