import pyautogui
import win32gui
import time
from CONST_VAR import *

RUNNING: bool = True  # 当程序需要关闭时，修改值为假


def press_key(key: str, window: int):
    """
    在窗口window内按住按键key.
    :param key: 按键
    :param window: 窗口句柄
    :return:
    """
    while RUNNING:  # 主程序未要求停止
        if win32gui.GetForegroundWindow() == window:  # 在指定窗口
            pyautogui.keyDown(key)
        else:
            pyautogui.keyUp(key)
        time.sleep(WAIT_TIME)  # 至少不会CPU 100%
    return 0
