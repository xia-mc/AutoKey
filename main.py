import gui
import keys
import threading as thread
from sys import exit

if __name__ == "__main__":
    try:
        targetWindow: int = gui.get_window_gui()  # 获取目标窗口句柄
    except SystemExit as err:
        print("程序已退出：执行前的用户操作")
        exit(0)

    # 开始Enter
    ExecThread: thread.Thread = thread.Thread(target=keys.press_key, args=("enter", targetWindow))
    ExecThread.start()

    # 等待结束
    gui.end_program_gui()  # 阻塞
    keys.RUNNING = False
    ExecThread.join()
    print("程序已退出：执行完成的用户操作")
    exit(0)

