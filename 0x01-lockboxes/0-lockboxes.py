#!/usr/bin/python3
"""
Author: Refiloe Radebe
Date: 10 October 2024
Description: This module contains a function that determines if all lockboxes
            can be unlocked based on the keys found within them.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked given a list of boxes with keys.

    Parameters:
            boxes (list of lists): A list where each index represents a box,
            and the value is list of keys found in that box.

    Returns:
            bool: True if all boxes can be unlocked,
            False otherwise.
    """
    # Number of boxes
    n = len(boxes)

    # A set to keep track of unlocked boxes
    # Box 0 is initially unlocked
    unlocked_boxes = set([0])
    # A stack to perform DFS, starting with box 0
    stack = [0]

    # Process the stack until it's empty
    while stack:
        # Pop the last box from the stack
        current_box = stack.pop()

        # Loop over all keys in the current box
        for key in boxes[current_box]:
            # If the key corresponds to a box number within bounds and the box is still locked
            if key < n and key not in unlocked_boxes:
                # Unlock the box
                unlocked_boxes.add(key)
                # Add the box to the stack for further exploration
                stack.append(key)

    # Return True if all boxes are unlocked
    return len(unlocked_boxes) == n
