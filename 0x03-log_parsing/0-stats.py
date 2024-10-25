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

import re
import sys


def extractInput(input_line):
    """
    Extracts sections of a line of an HTTP request log.
    """
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>[^]]+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)',
        r'\s*(?P<file_size>\d+)'
    )
    info = {
        'status_code': 0,
        'file_size': 0,
    }
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match is not None:
        status_code = resp_match.group('status_code')
        file_size = int(resp_match.group('file_size'))
        info['status_code'] = status_code
        info['file_size'] = file_size
    return info


def printStatistics(total_file_size, status_codes_stats):
    """
    Prints the accumulated statistics of the HTTP request log.
    """
    print('File size: {:d}'.format(total_file_size), flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)


def updateMetrics(line, total_file_size, status_codes_stats):
    """
    Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    """
    line_info = extractInput(line)
    status_code = line_info.get('status_code', '0')
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + line_info['file_size']


def run():
    """
    Starts the log parser.
    """
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        while True:
            line = sys.stdin.readline().strip()
            if not line:
                break
            total_file_size = updateMetrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                printStatistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        printStatistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
