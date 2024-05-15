"""
This script reads a .log file with messages in format:

'2024-01-22 08:30:01 INFO User logged in successfully.'

and counts the number of log messages at each level.

Example of usage from the command line:

python '/path/to/this_script.py' '/path/to/logfile' (to count count all logs in the log file)

python '/path/to/this_script.py' '/path/to/logfile' ERROR (additionaly to show all ERROR logs details)

"""


import sys


# function to parse a log line into a dictionary with date, time, level and message
def parse_log_line(line):
    parts = line.split()
    return {'date': parts[0], 'time': parts[1], 'level': parts[2], 'message': ' '.join(parts[3:])}

# function to load logs from a file into a list of dictionaries
def load_logs(file_path):
    try:
        with open(file_path, 'r') as file:
            return [parse_log_line(line) for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied when trying to read the file {file_path}.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred while reading the file {file_path}: {e}")
        sys.exit(1)

# function to filter logs by level
def filter_logs_by_level(logs, level):
    return [log for log in logs if log['level'].upper() == level.upper()]

# function to count logs by level
def count_logs_by_level(logs):
    count = {}
    for log in logs:
        level = log['level']
        if level in count:
            count[level] += 1
        else:
            count[level] = 1
    return count

# function to display log counts (as header)
def display_log_counts(counts):
    print("Logging Level - Count")
    print("---------------------")
    for level, count in counts.items():
        print(f"{level} - {count}")

# function to display detailed logs (for a specific level)
def display_detailed_logs(logs):
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

# main block to run the script
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a log file path.\n"\
              "run from command line: python '/path/to/this_script.py' '/path/to/logfile' -LEVEL(optional)")
        sys.exit(1)

    logs = load_logs(sys.argv[1])
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    # if a log level is provided as an argument, display detailed logs for that level
    if len(sys.argv) > 2:
        filtered_logs = filter_logs_by_level(logs, sys.argv[2])
        print(f"\nDetails of logs for the level '{sys.argv[2].upper()}':")
        display_detailed_logs(filtered_logs)

# run from command line with the log file path and optional log level argument: 
# 
# python 'script/path/script.py' 'log/path/log.log' INFO
#
# Output example:
#
# Logging Level - Count
# ---------------------
# INFO - 3
# ERROR - 1
# DEBUG - 2
#   
# Details of logs for the level 'INFO':
# 2024-01-22 08:30:01 - User logged in successfully.
# 2024-01-22 08:31:01 - User logged out.