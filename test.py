import win32api
import win32con

def on_shutdown(event):
    with open("test.txt", 'w') as file:
        file.write("shutdown event detected")


# Register the callback function for shutdown event
win32api.SetConsoleCtrlHandler(on_shutdown, True)

input("tf bitch")