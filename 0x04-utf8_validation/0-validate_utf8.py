#!/usr/bin/python3

"""
This module validates if a list of integers
represents a valid UTF-8 encoding.

"""


def validUTF8(data):
    # Number of bytes remaining in the current UTF-8 character
    remaining_bytes = 0

    for byte in data:
        # Only the last 8 bits are relevant, as each integer represents a byte
        byte &= 0xFF

        if remaining_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:  # 2-byte character
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                remaining_bytes = 3
            elif (byte >> 7) == 0b1:    # Invalid start of 2-byte character
                return False
        else:

            if (byte >> 6) != 0b10:
                return False
            remaining_bytes -= 1

    # If we're not expecting any more bytes, then it's valid UTF-8
    return remaining_bytes == 0
