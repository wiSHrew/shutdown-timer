from datetime import datetime, timedelta
import time
import tkinter
import tkinter.messagebox
import os

# get current time
def get_time():
    current_time = datetime.now()
    return current_time

# edit time.txt file
def edit_file(line_number, new_text):
    # Open the file in read mode
    with open("time.txt", 'r') as file:
        lines = file.readlines()

    # Modify the desired line
    if 1 <= line_number <= len(lines):
        lines[line_number - 1] = new_text + '\n'
    else:
        print(f"Line number {line_number} is out of range.")

    # Open the file in write mode and write the modified list back
    with open("time.txt", 'w') as file:
        file.writelines(lines)

#format line to something workable
def format_time(time):
    hour_str, minute_str, second_str = time.split(":")
    date_str, hour_str = hour_str.split(" ")
    year, month, day = date_str.split("-")

    formatted_time = [year, month, day, hour_str, minute_str, second_str]

    int_formatted_time = []
    for x in formatted_time:
        x = int(float(x))
        int_formatted_time.append(x)


    return int_formatted_time

# check if allowed to use and how much time is left
def last_session_check():
    with open("time.txt", 'r') as file:
        lines = file.readlines()

    last_session_start = format_time(lines[0])
    last_session_end = format_time(lines[1])
    time_now = format_time(str(get_time()))

    print(f"last session: {last_session_end}")
    print(f"time now: {time_now}")

    # check if same day, if not add 24 hours to time_now
    if last_session_end[1] < time_now[2]:
        time_now[3] = time_now[3] + 24

    #check if last 2 hours is used
    if lines[2] == "True":
        print("2 hours used")
        return "2 hours done, lol", False
    # check if 24 hours is done
    elif (time_now[3] - last_session_end[3]) <= 24:
        print("not 24 hours yet")
        return "wait 24 hours lol", False
    else:
        # check how much time left
        duration = []
        for i in range(3):
            i = i + 3
            if i == 5: # not counting the seconds
                break
            print(last_session_end[i])
            print(last_session_start[i])
            duration.append(last_session_end[i]-last_session_start[i])
        return duration, True

# check if duration is over
def check_duration(duration, start_time):
    current_time = get_time()
    time_passed = current_time - start_time
    time_over = False

    if time_passed > duration:
        time_over = True

    return time_over

# display messages
def msgbox(msg):
    window = tkinter.Tk()
    window.wm_withdraw()
    tkinter.messagebox.showinfo(title="lmaoooo", message=msg)
    window.destroy()
    return None

def shutdown_pc():
    os.system("shutdown /s /t 10")


# run everything
def pc_starts(duration):
    duration, allowed = last_session_check()
    if not allowed:
        shutdown_pc()
        msgbox(duration)
    
    if duration > 2:
        with open("time.txt", 'r') as file:
            lines = file.readlines()

        with open('error_logs.txt', 'a') as file:
            # Use the traceback.format_exc() function to get the full traceback as a string
            traceback_str = str(duration) + "\n"
            # Write the full traceback to the file
            file.write("duration was somehow more than 2 hours\n")
            file.write(traceback_str)
            file.writelines(lines)
            file.write("\n")

        msgbox(shutdown_pc)
        msgbox("idk wtf happened, tell me when you see this shit")
    
    start_time = get_time()
    edit_file(1, str(start_time))
    
    time_over = False
    # while not time_over:

    

duration = [3, 5]
