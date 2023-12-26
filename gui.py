import threading as thread
from time import sleep
import win32con
import win32api
import win32gui
from CONST_VAR import *


def MessageBox(returns: list[int], text: str, title: str = "", buttons: int = win32con.MB_OK, icon: int = 0):
    """
    (Win32Api, 适用于多线程)弹出消息框，在全局变量。阻塞
    :param returns: 指向返回值的变量
    :param text: 窗体内容
    :param title: 窗体标题，默认是空
    :param buttons: 按钮类型，默认是OK
    :param icon: 消息图标，默认是空
    :return: 1:确定 2:取消 3:终止 4:重试 5:忽略 6:是 7:否 10:再试一次
    """
    result: int = win32api.MessageBox(0, text, title, buttons, icon)
    returns[0] = result  # 想念指针了


class Tools:
    SelfWindow: int
    TargetWindow: int

    def get_first_window(self) -> int:
        """
        获取第一个不是本程序的窗口  *回滚功能
        :return: 窗口句柄
        """
        targetWindow = win32gui.GetForegroundWindow()
        self.SelfWindow = targetWindow

        while self.SelfWindow == targetWindow:
            targetWindow = win32gui.GetForegroundWindow()
            sleep(WAIT_TIME)

        self.TargetWindow = targetWindow
        return self.TargetWindow


# 初始化
tools: Tools = Tools()


def get_window_gui() -> int:
    """
    显示一个GUI，确认需要输入按键的窗口。阻塞
    :return: 窗口句柄
    """
    TipWindowResult: list[int] = [2]
    TipWindow: thread.Thread = thread.Thread(target=MessageBox,
                                             args=(TipWindowResult, "请切换到需要输入按键的窗口，然后单击确认", SELF_WINDOW_NAME, win32con.MB_OKCANCEL))
    TipWindow.start()
    sleep(WAIT_TIME)  # Anti-Bug
    FoundWindow = tools.get_first_window()
    TipWindow.join()

    if TipWindowResult[0] == 2:
        raise SystemExit("用户取消操作")
    return FoundWindow


def end_program_gui() -> None:
    """
    显示一个GUI，用于结束程序。阻塞
    :return:
    """
    TipWindow: thread.Thread = thread.Thread(target=win32api.MessageBox,
                                             args=(0, "单击\"确认\"以结束程序", SELF_WINDOW_NAME, win32con.MB_OK))
    TipWindow.start()
    TipWindow.join()


if __name__ == "__main__":
    get_window_gui()
