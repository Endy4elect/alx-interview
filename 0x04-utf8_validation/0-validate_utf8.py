#!/usr/bin/python3
"""
Method that determines if a given data set represents a valid UTF-8 encoding.
* Return: True if data is a valid UTF-8 encoding, else return False
* A character in UTF-8 can be 1 to 4 bytes long
* The data set can contain multiple characters
* The data will be represented by a list of integers
* Each integer represents 1 byte of data, therefore you only need
* to handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """validUTF8
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    valid = 0
    for value in data:
        byte = value & 255
        if valid:
            if byte >> 6 != 2:
                return False
            valid -= 1
            continue
        while (1 << abs(7 - valid)) & byte:
            valid += 1
        if valid == 1 or valid > 4:
            return False
        valid = max(valid - 1, 0)
    return valid == 0
