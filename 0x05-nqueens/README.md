
# 0x05. N Queens

## Overview

The **N Queens problem** is a classic challenge in computer science and mathematics that involves placing `N` non-attacking queens on an `N x N` chessboard. This project leverages the **backtracking algorithm** to find all possible solutions. It tests and enhances your understanding of recursion, list manipulations, and command-line argument handling in Python.

## Key Concepts

### 1. **Backtracking Algorithms**

- A systematic way to explore all potential solutions by recursively building and abandoning partial solutions that can't be completed.
- [Learn more about backtracking](https://en.wikipedia.org/wiki/Backtracking).

### 2. **Recursion**

- Used to implement the backtracking algorithm.
- Understand how functions can call themselves to explore solution spaces.

### 3. **List Manipulations in Python**

- Store and manipulate the positions of queens on the board.

### 4. **Command-Line Arguments**

- Handle user input for `N` using the `sys` module.

---

## Requirements

### General

- **Editors**: `vi`, `vim`, `emacs`
- Files will be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3` (version 3.4.3).
- Code must follow **PEP 8** style guidelines (version 1.7.*).
- Include a `README.md` file in the root directory of the project.
- All files must:
  - End with a new line.
  - Begin with `#!/usr/bin/python3`.
  - Be executable.

---

## Task: N Queens Solver

### Description

Write a Python program to solve the **N Queens problem**.

---

### Learning Objectives

- Implement a backtracking algorithm to solve a real-world problem.
- Develop recursive functions to explore and manage solution spaces.
- Use Python lists effectively for data storage and manipulation.
- Handle user input robustly through command-line arguments.

---

### Usage

```bash
./0-nqueens.py N
```

#### Input Validation

1. If the user provides the wrong number of arguments:

    ```bash
    Usage: nqueens N
    ```

    _Exit with status code `1`._

2. If `N` is not an integer:

    ```bash
    N must be a number
    ```

    _Exit with status code `1`._

3. If `N` is less than 4:

    ```bash
    N must be at least 4
    ```

    _Exit with status code `1`._

#### Output

- Print all possible solutions.
- Each solution is a list of `[row, column]` pairs where queens are placed.
- Format:

    ```bash
    [[row1, col1], [row2, col2], ...]
    ```

##### Example

**Input:**

```bash
./0-nqueens.py 4
```

**Output:**

```bash
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

**Input:**

```bash
./0-nqueens.py 6
```

**Output:**

```bash
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

---

## Author

- _Refiloe Radebe_
