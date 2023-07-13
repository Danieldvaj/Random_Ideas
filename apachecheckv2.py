import time
import re
import os

def parse_log_file(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()

    error_pattern = r'Active: Error \(running\) since ([\w\s:\-]+)'
    active_pattern = r'Active: active'

    for log in logs:
        error_match = re.search(error_pattern, log)
        if error_match:
            date_str = error_match.group(1)
            print(f"There has been an error with the following date: {date_str}")
            continue

        active_match = re.search(active_pattern, log)
        if active_match:
            print('.')
            continue

def monitor_log_file(log_file, interval=60):
    while True:
        if os.path.exists(log_file):
            parse_log_file(log_file)
        else:
            print(f"Log file {log_file} does not exist.")
        time.sleep(interval)

monitor_log_file('path/to/your/logfile.log')
