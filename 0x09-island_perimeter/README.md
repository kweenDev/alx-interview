
# Island Perimeter Algorithm

## Overview

This repository contains the solution for the **Island Perimeter** project, which involves calculating the perimeter of an island in a grid. The grid is represented as a 2D array of integers where:

- `1` represents land.
- `0` represents water.

The goal is to compute the perimeter of the land (the island) in the grid, taking into account only the edges that are exposed to water (either at the edge of the grid or adjacent to water cells).

---

## Problem Description

The task is to implement the function `island_perimeter(grid)` that calculates the perimeter of the island described in the grid. The island is surrounded by water, and the grid will not contain any lakes (no water inside the island). The grid is rectangular and does not exceed 100 in width or height.

### Constraints

- `grid` is a list of lists (2D array).
- Each cell represents either water (`0`) or land (`1`).
- Each cell is a square with a side length of 1.
- Land cells are connected horizontally or vertically (not diagonally).
- The grid is surrounded entirely by water.
- The grid contains only one island or nothing.
- No lakes are present inside the island.

**Example:**

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```

For the above grid, the expected output is `12` since the island has a perimeter of 12 units.

---

## Concepts Utilized

### 2D Arrays (Matrices)

- Accessing and iterating over elements in a 2D array.
- Navigating through adjacent cells (horizontally and vertically).

### Conditional Logic

- Identifying whether a cell contributes to the perimeter by checking its adjacent cells.
- Counting edges that contribute to the perimeter.

### Problem-Solving Strategies

- Breaking the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.
- Using nested loops and conditional statements for iteration and logic.

### Function Signature

```python
def island_perimeter(grid: List[List[int]]) -> int:
```

**Parameters:**

- `grid`: A 2D list of integers where `1` represents land and `0` represents water.

**Returns:**

- The perimeter of the island (integer).

---

## Approach

To solve this problem, we need to iterate over each land cell (`1`) in the grid and check its neighboring cells (up, down, left, right). If a neighboring cell is water (`0`) or out of bounds, it contributes to the perimeter.

**Steps:**

1. Initialize a variable `perimeter` to zero.
2. Loop through each cell in the grid.
3. For each land cell, check its four neighbors.
4. For each neighbor that is water or out of bounds, increment the perimeter.
5. Return the final perimeter after completing the iteration.

**Example Usage:**

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid)) # Output: 12
```

---

## File Structure

```plaintext
0x09-island_perimeter/
│
├── 0-island_perimeter.py     # Function to calculate island perimeter
├── 0-main.py                 # Driver code to test the function
├── README.md                 # Project documentation
└── 0x09-Report.md            # Project summary and challenges
```

---

## Author

- _Refiloe Radebe_
