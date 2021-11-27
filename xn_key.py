"""
这里的都是高级的键盘输入(驱动级)
"""

import keyboard
from time import sleep

# 按 n 键    
def press(n:str):
    """[这个是按下然后抬起的]

    Args:
        n (str): [description]
    """
    keyboard.press_and_release(n)
    sleep(0.1)


# 按下 n 键
def press_down(n:str):
    """[这个是按下,然后不松开]

    Args:
        n (str): [按下哪个键]
        t (int): [持续多久]
    """
    keyboard.press(n)
    
# 松开 n 键
def press_up(n:str):
    """[这个是松开]

    Args:
        n (str): [按下哪个键]
        t (int): [持续多久]
    """
    keyboard.release(n)


# 按下 n 键
def press_down_t(n:str, t:int):
    """[这个是按下,然后过段时间松开]

    Args:
        n (str): [按下哪个键]
        t (int): [持续多久]
    """
    keyboard.press(n)
    sleep(t)
    keyboard.release(n)

if __name__ == '__main__':
    press_down(' ', 1)
    # press('space')
    
