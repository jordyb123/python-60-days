import os
import datetime

LOG_FILE = "log.txt"

def log_message(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} | {message}\n")
    print("Log entry added")

def view_log():
    if not os.path.exists(LOG_FILE):
        print("No log file found.")
        return
    
    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    if not lines:
        print("Log is empty")
        return

    for line in lines:
        print(line.strip())

def clear_log():
    with open(LOG_FILE, "w") as f:
        pass
    print("Log cleared.")