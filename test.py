import traceback

try:
    # Your code that may raise an exception goes here
    time_now = [1, 2, 3, 4]  # Example code that raises a TypeError
    time_now[3] = time_now + 24  # This will raise a TypeError
except Exception as e:
    # Open a file in write mode ('w')
    with open('error_logs.txt', 'a') as file:
        # Use the traceback.format_exc() function to get the full traceback as a string
        traceback_str = traceback.format_exc() + '\n'
        # Write the full traceback to the file
        file.write(traceback_str)