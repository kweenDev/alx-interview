# 0x01. Lockboxes

## Description

This project involves solving the **Lockboxes** problem using Python. The problem requires determining if all the boxes in front of you can be unlocked. Each box contains keys that unlock other boxes, and box 0 is always unlocked initially. The goal is to create an efficient algorithm to check whether all the boxes can eventually be unlocked given the available keys.

Thos problem can be approached using graph traversal techniques, such as Depth-First Search (DFS), where each box is treated as a node, and keys are edges connecting these nodes.

## Concepts Involved

1. **List Manipulation**:

   - You need to iterate over lists, access elements, and dynamically track the state of unlocked boxes.

2. **Graph Theory**:

   - The boxes and keys can be visualized as a graph, where each box is a node, and keys provide the connections (edges) between nodes.

3. **Algorithm Design**:

   - The algorithm needs to be efficient in terms of time and space complexity to handle all test cases.

4. **Recursion and Iteration**:

   - DFS or BFS algorithms are suitable for traversing the boxes and unlocking them as we go along.

5. **Set Operations**:
   - Sets are used to keep track of the boxes that have already been unlocked for fast look-up.

## Requirements

- All code is written in Python 3.4.3 and tested on Ubuntu 20.04 LTS.
- Code follows **PEP 8** standards for Python code style.
- The project must contain the following:
  - An executable Python script: `0-lockboxes.py`
  - A test script to validate the solution: `main_0.py`
  - A `README.md` file documenting the project.

## File Structure

```text
0x01-lockboxes
├── README.md            # Project description and usage instructions
├── 0-lockboxes.py       # Python script with the solution to the problem
└── main_0.py            # Script to test the solution
```

## Prototype

```python
def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked given a list of boxes with keys.

    Parameters:
    boxes (list of lists): A list where each index represents a box, and the value is a
                           list of keys found in that box.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
```

## How to Use

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/kweendev/alx-interview.git
   cd alx-interview/0x01-lockboxes
   ```

2. Ensure that the Python version being used is compatible (Python 3.4.3 or later).

3. Make sure the Python scripts are executable:
   ```bash
   chmod +x 0-lockboxes.py main_0.py
   ```

### Running the Code

- To test the function with the provided test cases, simply run the `main_0.py` file:

  ```bash
  ./main_0.py
  ```

- Example Output:
  ```bash
  True
  True
  False
  ```

### Example Usage

- Here is an example of the boxes setup and function call:
  ```python
  boxes = [[1], [2], [3], [4], []]
  print(canUnlockAll(boxes))  # Output: True
  ```
- This test case shows that all boxes can be opened sequentially using the keys available in each unlocked box.

## Test Cases

The following test cases have been provided to verify the functionality of the program:

- **Test Case 1**: All boxes can be unlocked.

```python
boxes = [[1], [2], [3], [4], []]
# Output: True
```

- **Test Case 2**: All boxes can be unlocked with extra keys.

```python
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# Output: True
```

- **Test Case 3**: Not all boxes can be unlocked.

```python
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# Output: False
```

## Algorithm Explanation

The solution uses a **_Depth-First Search_** (DFS) algorithm to traverse through the boxes starting from Box 0 (which is always unlocked). We keep track of unlocked boxes in a set and explore the keys inside each box using a stack.

The steps involved are as follows:

1. Initialize an `unlocked_boxes` set starting with Box 0.
2. Use a stack to explore keys in each unlocked box.
3. For each box, check the keys it contains. If a key corresponds to a box number, unlock that box (if not already unlocked) and explore the keys within it.
4. Continue this process until no more boxes can be unlocked.
5. If all boxes are unlocked by the end, return `True`, otherwise return `False`.

### Edge Cases

- If there is only one box (`boxes = [[]]`), the function will return `True` since there is nothing else to unlock.
- If there are keys that do not correspond to any box (keys greater than the number of boxes), the function will ignore those keys.
- If some boxes are inaccessible because their keys are inside a box that is never unlocked, the function will return `False`.

### Complexity

- **Time Complexity**: O(n + m), where `n` is the number of boxes and `m` is the total number of keys.
- **Space Complexity**: O(n), since we are using a set to track unlocked boxes and a stack to manage the DFS.

## Author

_Refiloe Radebe_
