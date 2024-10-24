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
import signal

# Initialize counters and data structures
total_file_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_stats(status_codes, total_size):
    """
    Prints the current statistics:
    - Total file size
    - Count of status codes that have appeared
    Args:
        status_codes (dict): Dictionary of status code counts
        total_size (int): Total file size accumulated so far
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def handle_interrupt(signal, frame):
    """
    Signal handler for keyboard interruption (CTRL + C).
    This function prints the final statistics before exiting the program.
    """
    print_stats(status_codes_count, total_file_size)
    sys.exit(0)


# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, handle_interrupt)

try:
    # Process log entries from standard input
    for line in sys.stdin:
        line_count += 1
        try:
            parts = line.split()
            if len(parts) > 6:
                # Extract status code and file size from the log line
                status_code = parts[-2]
                file_size = int(parts[-1])

                # Update total file size
                total_file_size += file_size

                # Update the count for the status code if it's valid
                if status_code in status_codes_count:
                    status_codes_count[status_code] += 1

        except (IndexError, ValueError):
            # Skip the line if it doesn't conform to the expected format
            continue

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_stats(status_codes_count, total_file_size)

except KeyboardInterrupt:
    # Handle keyboard interrupt during processing
    print_stats(status_codes_count, total_file_size)
    sys.exit(0)

# Print final statistics if end of input is reached
print_stats(status_codes_count, total_file_size)
