
# 0x03. Log Parsing

## Project Overview

**Project Name:** 0x03. Log Parsing  
**Project Weight:** 1  
**Start Date:** October 21, 2024, 6:00 AM  
**End Date:** October 25, 2024, 6:00 AM  
**Language:** Python  
**Platform:** Ubuntu 20.04 LTS  
**GitHub Repository:** alx-interview  
**Directory:** `0x03-log_parsing`

The **0x03. Log Parsing** project requires you to write a Python script that reads log data from **standard input (stdin)**, processes the data in real-time, and computes metrics such as total file size and status code counts. This task emphasizes efficient log parsing, real-time data handling, and regular monitoring of system performance.

## Project Requirements

- All code should be written in **Python**.
- All Python files should adhere to **PEP 8** style guidelines.
- The script must be executable and start with `#!/usr/bin/python3`.
- It should handle the expected input format and skip invalid or malformed lines.
- Metrics must be printed after every **10 lines** or upon **keyboard interruption (CTRL + C)**.

## Concepts Utilized

### 1. **File I/O in Python**
   - Reading input line by line from `sys.stdin`.
   - Handling real-time input using `input()` or `sys.stdin`.

### 2. **Signal Handling**
   - Capture and handle interruptions like **CTRL + C** using Python’s `signal` module.

### 3. **Data Parsing**
   - Extract IP address, status code, and file size from log lines.
   - Use **regular expressions** to validate and ensure correct format.

### 4. **Data Processing & Aggregation**
   - Use **dictionaries** to count occurrences of status codes.
   - Continuously sum up total file size from valid log entries.

### 5. **Exception Handling**
   - Use `try-except` blocks to manage unexpected inputs without crashing the program.

## Input Format

Each log entry must follow this format:

    ```bash
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    ```

### Example

    ```bash
    192.168.1.10 - [2024-10-24 15:35:30] "GET /projects/260 HTTP/1.1" 200 512
    ```

- **IP Address**: 192.168.1.10  
- **Date**: [2024-10-24 15:35:30]  
- **Request**: "GET /projects/260 HTTP/1.1"  
- **Status Code**: 200  
- **File Size**: 512  

## Task Description

### Task 0: Log Parsing

#### Task Summary:
You must write a Python script that reads log entries from `stdin`, parses them, and prints useful statistics.

#### Task Details:

1. **Input Handling**:
    - Read lines one by one from `stdin`.
    - Skip lines that do not conform to the expected format.

2. **Metrics Computed**:
    - **Total File Size**: The sum of all file sizes from valid lines.
    - **Status Code Count**: Count occurrences of these status codes:
      - 200, 301, 400, 401, 403, 404, 405, 500

3. **Output Requirements**:
    - After every 10 lines or a keyboard interruption, output:
      ```
      File size: <total file size>
      <status code>: <number of occurrences>
      ```
    - Status codes should be printed in **ascending order**, only if they appeared.

4. **Handling Interruptions**:
    - Capture `CTRL + C` and print the current statistics before exiting.

#### Example Output:

    ```bash
    File size: 5213 200: 2 401: 1 403: 2 404: 1 405: 1 500: 3
    ```

## Installation & Usage

1. Clone the repository from GitHub:

    ```bash
    git clone https://github.com/your_username/alx-interview.git
    cd 0x03-log_parsing
    ```

2. Make the script executable:

    ```bash
    chmod +x 0-stats.py
    ```

3. Run the log generator and pipe the output to your parser:

    ```bash
    ./0-generator.py | ./0-stats.py
    ```

4. You can also test the script using a custom log file:

    ```bash
    cat sample_log.txt | ./0-stats.py
    ```

## Sample Test Case

Here’s a sample input that the script should handle:

    ```bash
    192.168.1.10 - [2024-10-24 15:35:30] "GET /projects/260 HTTP/1.1" 200 512 172.16.0.5 - [2024-10-24 15:35:32] "GET /projects/260 HTTP/1.1" 404 1024
    ```

Expected output:

    ```bash
    File size: 1536 200: 1 404: 1
    ```

## Edge Cases

- **Malformed Log Lines**: The script should skip any lines that do not match the expected format.
- **Unknown Status Codes**: Only the specified status codes should be printed. Unknown status codes are ignored.

## Resources

- [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)
- [Python Regular Expressions](https://docs.python.org/3/library/re.html)
- [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python Exception Handling](https://docs.python.org/3/tutorial/errors.html)

## Author

**Name**: Refiloe Radebe
**Date**: October 21, 2024  
**Repository**: [GitHub Repository](https://github.com/kweenDev/alx-interview)
