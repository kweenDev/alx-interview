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


def print_stats():
    """
    Prints the current statistics:
    - Total file size
    - Count of status codes that have appeared
    """
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_dict.keys()):
        if status_codes_dict[code] > 0:
            print(f"{code}: {status_codes_dict[code]}")


def handle_interrupt(signal, frame):
    """
    Signal handler for keyboard interruption (CTRL + C).
    This function prints the final statistics before exiting the program.
    """
    print_stats()
    sys.exit(0)


# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, handle_interrupt)


try:
    # Process log entries from standard input
    for line in sys.stdin:
        try:
            parts = line.split()
            # Ensure that the line has the correct format
            if len(parts) < 7:
                continue

            # Extract status code and file size from the log line
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update total file size
            total_file_size += file_size

            # Update the count for the status code if it's valid
            if status_code in status_codes_dict:
                status_codes_dict[status_code] += 1

            # Update line count
            line_count += 1

            # Print statistics after every 10 lines
            if line_count == 10:
                print_stats()
                line_count = 0

        except (IndexError, ValueError):
            # Skip the line if it doesn't conform to the expected format
            continue

except KeyboardInterrupt:
    # Handle keyboard interrupt during processing
    print_stats()
    sys.exit(0)

# Print final statistics if end of input is reached
print_stats()
