import time
import win32api
import win32con
import win32gui
import pyautogui
from ctypes import windll



VK_CODE = {'q': 0x51, 'w': 0x57, 'e': 0x45, 'r': 0x52, 'd': 0x44, 'f': 0x46, 'b': 0x42, 'p': 0x50, 'y': 0x59,
           'esc': 0x1B, 'F1': 0x70}

X = 500
Y = 500


# 鼠标移动
def mouse_move(x, y):
    """
        pyautogui API:
        pyautogui.moveTo(x, y)
        pyautogui.click()

        win32api API:
        windll.user32.SetCursorPos(x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    """
    # windll.user32.SetCursorPos(x, y)
    pyautogui.moveTo(x, y)
    time.sleep(0.01)


# 鼠标点击
def mouse_click(x, y, button=1):
    mouse_move(x, y)
    if button == 1:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    else:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)


# 键盘控制
def key_press(vk_code):
    win32api.keybd_event(vk_code, 0, 0, 0)
    win32api.keybd_event(vk_code, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.01)


# 定位点击
def locking_screen(imgName, button=1):
    try:
        # 在当前屏幕中查找指定图片(图片需要由系统截图功能截取的图)
        coords = pyautogui.locateOnScreen(imgName)
        # 获取定位到的图中间点坐标
        x, y = pyautogui.center(coords)

        # 左击or右击
        if button == 1:
            print(imgName.replace('.png', ' 左击...'))
            mouse_click(x, y, button)
        else:
            print(imgName.replace('.png', ' 右击...'))
            mouse_click(x, y, 2)
        mouse_move(X, Y)
        return True
    except:
        # print(imgName + ":error")
        return False


# 定位点击 循环1秒1次
def locking_screen_while(imgName, button=1):
    print("循环执行:" + imgName)
    while True:
        locking_screen(imgName, button)
        time.sleep(1)


# 游戏窗口
def lol_client():
    """
        大厅界面窗口: "League of Legends"
        游戏界面窗口: "League of Legends (TM) Client"
    """
    try:
        # win_name_lol = "League of Legends"
        win_name_lol_client = "League of Legends (TM) Client"
        # 窗口的类名可以用Visual Studio的SPY++工具获取
        hwnd = win32gui.FindWindow(0, win_name_lol_client)
        # 获取句柄窗口的大小信息
        left, top, right, bot = win32gui.GetWindowRect(hwnd)
        return left, top
    except:
        return 0, 0


# 游戏开始
def lol_play():
    """
        上坐标: left+1323, top+754 中坐标: left+1268, top+699 下坐标: left+1203, top+634
    """
    print("play")
    while True:
        # 判断游戏界面载入成功
        try:
            print("游戏开始...")

            left, top = lol_client()
            topXY, midXY, supXY = (left + 1203, top + 634), (left + 1268, top + 699), (left + 1323, top + 754)

            # 购买装备
            lol_buy(X, Y)

            print("开始移动:")

            # 移动到上路
            mouse_click(topXY[0], topXY[1], button=3)
            key_press(VK_CODE['a'])
            time.sleep(30)

            # 移动到中路
            mouse_click(midXY[0], midXY[1], button=3)
            key_press(VK_CODE['a'])
            time.sleep(30)

            # 移动到下路
            mouse_click(supXY[0], supXY[1], button=3)
            key_press(VK_CODE['a'])
            time.sleep(30)
        except:
            print("游戏结束...")


# 商店购买
def lol_buy(x, y):
    """
    mouse_move(x, y) 复位鼠标，防止装备提示信息阻挡定位
    """
    print("打开商店...")
    pyautogui.middleClick()
    key_press(VK_CODE['y'])

    buy1 = locking_screen('lol_buy1.png', 2)
    if buy1:
        print("购买推荐1")
        mouse_move(x, y)
        time.sleep(0.5)

    buy2 = locking_screen('lol_buy2.png', 2)
    if buy2:
        print("购买推荐2")
        mouse_move(x, y)
        time.sleep(0.5)

    buy3 = locking_screen('lol_buy3.png', 2)
    if buy3:
        print("购买推荐3")
        mouse_move(x, y)
        time.sleep(0.5)

    print("关闭商店...")
    key_press(VK_CODE['esc'])


# 游戏结束
def lol_over():
    left, top = lol_client()
    return left == 0 & top == 0


if __name__ == '__main__':
    lol_play()
    # lol_buy(50,50)
    # lol_play("")
    # locking_screen_while('lol_findGame.png')
    # locking_screen('tt_jiaoyue.png')
    # mouse_move(1016, 829)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    # mouse_click(1016,829)y
    # while True:
    #     time.sleep(0.5)
    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    #     time.sleep(0.5)
    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)y