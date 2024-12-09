
# 0x08. Making Change

## Algorithm | Python

---

### Overview

For the **“0. Change comes from within”** project, you will tackle a classic problem in the domain of **dynamic programming** and **greedy algorithms**: the **coin change problem**. The goal is to determine the minimum number of coins required to make up a given total amount, provided a list of coin denominations.

This project will test your ability to develop algorithms that are:

- **Correct**: Produce the desired results for all inputs.
- **Efficient**: Meet runtime and space constraints.

---

### Key Concepts

#### Greedy Algorithms

- Learn how greedy algorithms work and why they may be suitable for the coin change problem.
- Understand the limitations of greedy approaches, especially when they may not yield the optimal solution.

#### Dynamic Programming

- Master the principles of **dynamic programming** as a technique for solving optimization problems.
- Understand concepts such as:
  - **Overlapping subproblems**
  - **Optimal substructure**

#### Algorithmic Complexity

- Analyze **time** and **space complexity** of algorithms.
- Strive for solutions with minimal computational overhead.

#### Problem-Solving Strategies

- Break down problems into smaller, manageable sub-problems.
- Explore **iterative** vs **recursive** approaches to dynamic programming.

#### Python Programming

- Utilize Python lists and list comprehensions effectively.
- Implement functions with efficient loops and conditional statements.

---

### Requirements

#### General

- **Allowed editors**: `vi`, `vim`, `emacs`
- **Execution Environment**: Ubuntu 20.04 LTS, Python 3.4.3
- All files should:
  - End with a new line.
  - Start with `#!/usr/bin/python3`.
  - Follow **PEP 8** style guidelines (version 1.7.x).
  - Be executable.
- A `README.md` file is mandatory and must be located at the root of the project directory.

---

### Tasks

#### 0. Change comes from within

**Objective:**
Given a pile of coins of different values, determine the **fewest number of coins** needed to meet a given total amount.

#### Prototype

```python
def makeChange(coins, total):
```

#### Returns

- The fewest number of coins needed to meet `total`.
- `0` if `total` is `0` or less.
- `-1` if the total cannot be met with the given coins.

#### Constraints

- `coins` is a list of integers greater than `0` (coin denominations).
- Infinite number of each coin denomination is available.
- Solution runtime will be evaluated.

#### Example

```python
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

### Resources

- **Key Articles:**
  - [GeeksforGeeks: Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [GeeksforGeeks: Greedy Algorithm to find Minimum Number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)

- **Videos:**
  - [YouTube: Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=Y0ZqKpToTic)

- **Python Documentation:**
  - [Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)

---

### Repository Details

- **GitHub Repository:** `alx-interview`
- **Directory:** `0x08-making_change`
- **File:** `0-making_change.py`

---

### Author

- *Refiloe Radebe*
