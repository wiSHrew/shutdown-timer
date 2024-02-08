import win32api
import win32con

def on_shutdown(event):
    with open("shutdown_log.txt", "a") as file:
        file.write("System is shutting down...\n")

# Register the callback function for shutdown event
win32api.SetConsoleCtrlHandler(on_shutdown, True)

# Keep the program running
input("Press Enter to exit...")
