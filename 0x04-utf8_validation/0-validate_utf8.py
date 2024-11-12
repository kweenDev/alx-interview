#!/usr/bin/python3
"""
Author: Refiloe Radebe (kweenDev)
Date: 12 November, 2024
Description: This script checks if a given data set is a valid UTF-8 encoding.
The validUTF8 function uses bitwise operations to validate each byte
according to UTF-8 encoding rules for 1-4 byte sequences.
"""


def validUTF8(data):
    """
    Validate if data is a valid UTF-8 encoding.

    Args:
        data (list of int): List of integers representing bytes in the
        data set.

    Returns:
        bool: True if data is a valid UTF-8 encoding, False otherwise.
    """
    # Tracks how many bytes are left in the current UTF-8 character
    num_bytes = 0

    # Define bit masks
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Only look at the least significant 8 bits of the integer
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & mask1) == 0:
                # 1-byte character (ASCII), no additional bytes needed
                continue
            elif (byte & (mask1 >> 1)) == mask1:
                num_bytes = 1
            elif (byte & (mask1 >> 2)) == mask1:
                num_bytes = 2
            elif (byte & (mask1 >> 3)) == mask1:
                num_bytes = 3
            else:
                return False
        else:
            # Check that the byte is a valid continuation byte (10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False
        # Decrement the byte count
        num_bytes -= 1

    return num_bytes == 0
