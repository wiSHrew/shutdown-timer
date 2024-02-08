import win32api
import win32con

def hello(event):
    with open("test.txt", 'w') as file:
        file.write("hello")

win32api.SetConsoleCtrlHandler(hello, True)

hello()
input("tf bitch")