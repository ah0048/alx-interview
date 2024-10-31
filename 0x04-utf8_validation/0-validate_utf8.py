#!/usr/bin/python3
'''validate if data is UTF-8 encoded'''


def validUTF8(data):
    '''validate if data is UTF-8 encoded'''
    valid = True
    for byte in data:
        if byte > 255:
            valid = False
            break
    return valid
