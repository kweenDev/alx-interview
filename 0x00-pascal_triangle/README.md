# Pascal's Triangle

## Project Overview

This project contains an algorithm to generate Pascal's Triangle up to a given number of rows. Pascal's Triangle is a triangular array of the binomial coefficients that arise in combinatorics. Each number is the sum of the two directly above it.

### Pascal's Triangle Example (n=5)

    ```csharp
    [1]
    [1,1]
    [1,2,1]
    [1,3,3,1]
    [1,4,6,4,1]
    [1,5,10,10,5,1]
    ```

## Learning Objectives

The key concepts covered in this project include:

- List Comprehensions
- Function Definitions
- Looping (For Loops)
- Conditional Statements
- Arithmetic Operations
- Memory Management

## Files

1. **`0-pascal_triangle.py`**: Contains the implementation of Pascal's Triangle.
2. **`main.py`**: A sample script to test the functionality of the Pascal's Triangle function.

## Requirements

- Python 3.x
- List data structure knowledge
- Basic arithmetic and combinatorial understanding

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/kweenDev/alx-interview.git
   cd 0x00-pascal_triangle
   ```

2. Run the main script to see the Pascal's Triangle for 5 rows:
   ```bash
   python3 main.py
   ```

## Usage

You can generate Pascal's Triangle for any number of rows by calling the pascal_triangle(n) function with your desired number of rows.

### Example:

    ```python
    from pascal_triangle import pascal_triangle

    triangle = pascal_triangle(7)
    print(triangle)

    ```

### Example Output:

    ```csharp
    [1]
    [1,1]
    [1,2,1]
    [1,3,3,1]
    [1,4,6,4,1]
    [1,5,10,10,5,1]
    ```

## Author

Refiloe Radebe - Date: 2024-10-07
