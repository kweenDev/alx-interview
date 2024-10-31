
# 0x04. UTF-8 Validation Project

![UTF-8 Validation](https://images.unsplash.com/photo-1514846326710-096381256f65?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MXwyMDQ1NXwwfDF8c2VhcmNofDJ8fFVURi04JTIwZW5jb2Rpbmd8ZW58MHx8fHw&ixlib=rb-1.2.1&q=80&w=400)

## Overview

This project focuses on validating whether a given dataset represents a valid UTF-8 encoding. UTF-8 is a variable-width character encoding standard that can represent every character in the Unicode character set. The objective is to design a function using Python that reads a list of integers and checks if each byte sequence adheres to UTF-8 encoding rules. Mastery of bitwise operations, data representation at the byte level, and logical problem-solving will be essential.

---

## Project Requirements

- **Language**: Python 3.4.3
- **Platform**: Ubuntu 20.04 LTS
- **File Requirements**:
  - All code should end with a new line and be PEP 8 compliant.
  - The `README.md` file must be included.
  - Make sure all files are executable.

---

## Learning Objectives

This project sharpens understanding and application of:

1. **Bitwise Operations**: Understanding operators such as AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), and shifts (`<<`, `>>`).
2. **UTF-8 Encoding**: Comprehension of UTF-8 encoding rules for 1-4 byte characters.
3. **Data Representation**: Byte-level data handling and manipulation.
4. **Boolean Logic and List Manipulation**: Essential for iterating through byte data to validate sequences.

---

## Function Prototype

The function to implement:

```python
def validUTF8(data: list[int]) -> bool:
    """
    Validates if the input list of integers represents a valid UTF-8 encoding.

    Args:
        data (list[int]): List of integers where each integer represents a byte.

    Returns:
        bool: True if data is valid UTF-8 encoding, False otherwise.
    """
```

---

## Task Details

### Task 0: UTF-8 Validation (Mandatory)

Create a function `validUTF8(data)` that:

- Accepts a list of integers as input.
- Returns `True` if the data is a valid UTF-8 encoding; otherwise, `False`.
- Handles encoding validation for UTF-8 characters ranging from 1 to 4 bytes.

---

### UTF-8 Encoding Rules

1. A 1-byte character is represented by `0xxxxxxx`.
2. A 2-byte character starts with `110xxxxx` followed by `10xxxxxx`.
3. A 3-byte character starts with `1110xxxx` followed by two `10xxxxxx` bytes.
4. A 4-byte character starts with `11110xxx` followed by three `10xxxxxx` bytes.

Any deviation from these patterns results in an invalid UTF-8 encoding.

### Example Usage

To test the `validUTF8` function, save the following sample code as `0-main.py`:

```python
#!/usr/bin/env python3
"""
Main file for testing UTF-8 validation
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]  # ASCII character 'A', valid UTF-8
print(validUTF8(data))  # Expected output: True

data = [229, 65, 127, 256]  # Contains an out-of-range byte (256)
print(validUTF8(data))  # Expected output: False
```

---

## Project Files

- `0-validate_utf8.py`: Contains the `validUTF8` function.
- `README.md`: Project documentation.

## Setup & Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/kweenDev/alx-interview.git
    ```

2. Navigate to the project directory:

    ```bash
    cd alx-interview/0x04-utf_validation
    ```

3. Run the test script:

    ```bash
    ./0-main.py
    ```

---

## Author

Refiloe Radebe (_kweenDev_): A software engineering student with a passion for solving complex problems through code.
