# 0x02. Minimum Operations

## Description

This project focuses on developing an algorithm that calculates the minimum number of operations required to generate exactly `n` characters in a text file. The text file starts with a single character `H`, and the only two allowed operations are:

- **Copy All**: Copies all characters in the file.
- **Paste**: Pastes the copied characters.

The task is to determine how to use the least number of operations to produce exactly `n` characters.

## Concepts Required

To solve this problem efficiently, the following concepts are necessary:

- **Dynamic Programming**: For breaking the problem into smaller subproblems.
- **Prime Factorization**: The number of operations can be related to the prime factors of `n`.
- **Greedy Algorithms**: Choosing the best option at each step might simplify the solution.
- **Basic Python Programming**: Knowledge of loops, conditionals, and functions is required for implementation.

## Prototype

```python
def minOperations(n):
    """
    Calculate the minimum number of operations required to reach exactly n 'H' characters.

    Parameters:
    n (int): Target number of 'H' characters

    Returns:
    int: Minimum number of operations or 0 if it's not possible
    """
```

**Example**
\_For `n = 9`:

```plaintext
H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
```

#### Number of operations: 6

\_For `n = 12`:

```plaintext
H => Copy All => Paste => HH => Copy All => Paste => HHHH => Paste => HHHHHHHHHHHH
```

#### Number of operations: 7

## Files

- `0-minoperations.py`: Contains the implementation of the `minOperations` function.
- `0-main.py`: A test file to run the function with sample inputs.

## Usage

To run the program:

1. Clone the repository:

```bash
git clone https://github.com/kweenDev/alx-interview.git
```

2. Navigate to the project directory:

```bash
cd alx-interview/0x02-minimum_operations
```

3. Run the script:

```bash
./0-main.py
```

## Requirements

- All files will be interpreted on Ubuntu 20.04 LTS using `python3`.
- Code must conform to PEP 8 style guidelines (version 1.7.x).
- All scripts must be executable.
- A `README.md` file is mandatory in the root of the project folder.

## Author

- Refiloe Radebe (_kweenDev_)
- Date: 2024-10-16
