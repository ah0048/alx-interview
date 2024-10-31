#!/usr/bin/python3
'''validate if data is UTF-8 encoded'''


def validUTF8(data):
    '''validate if data is UTF-8 encoded'''
    remaining_bytes = 0
    for byte in data:
        byte = byte & 0b11111111
        if remaining_bytes == 0:
            if byte >> 5 == 0b110:
                remaining_bytes = 1
            elif byte >> 4 == 0b1110:
                remaining_bytes = 2
            elif byte >> 3 == 0b11110:
                remaining_bytes = 3
            elif byte >> 7 == 0b0:
                continue
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            remaining_bytes -= 1

    return remaining_bytes == 0
