#!/usr/bin/python3
"""
Log Parsing Script

This script reads log entries from standard input (stdin) line by line and
computes statistics related to the log entries, such as total file size and
occurrences of various HTTP status codes. The script prints the statistics
after every 10 lines or upon a keyboard interruption (CTRL + C).

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Author: Refiloe Radebe
Date: October 21, 2024
"""


import sys


# Initialize counters and data structures
status_codes_dict = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
total_file_size = 0
line_count = 0


try:
    # Process log entries from standard input
    for line in sys.stdin:
        line_count = line.split(" ")

        if len(line_count) > 4:
            # Extract status code and file size from the log line
            status_code = line_count[-2]
            file_size = int(line_count[-1])

            # Update the count for the status code if it's valid
            if status_code in status_codes_dict.keys():
                status_codes_dict[status_code] += 1

            # Update total file size
            total_file_size += file_size

            # Update line count
            line_count += 1

        # Print statistics after every 10 lines
        if line_count == 10:
            line_count = 0
            print('File size: ()'.format(total_file_size))

            # Print status code counts
            for key, value in sorted(status_codes_dict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as KeyboardInterrupt:
    pass

finally:
    print('File size: {}'.format(total_file_size))
    for key, value in sorted(status_codes_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
