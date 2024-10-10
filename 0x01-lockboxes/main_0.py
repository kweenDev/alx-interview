#!/usr/bin/python3
"""
Author: Refiloe Radebe
Date: 10 October 2024
Description: This script tests the
canUnlockAll function with sample input.
"""

canUnlockAll = __import__('0-lockboxes').canUnlockAll

# Test case 1: All boxes can be unlocked
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Expected output: True

# Test case 2: All boxes can be unlocked with extra keys
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2][3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Expected output: True

# Test case 3: Not all boxes can be unlocked
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Expected output: False
