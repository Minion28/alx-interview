#!/usr/bin/python3

"""
method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8_v1(data):
    """
    Return: True if data is a valid UTF-8 encoding, else return False
    """
    x = 0
    if not data:
        return False
    for number in data:
        bin_rep = format(number, '#010b')[-8:]

        if x == 0:
            for bit in bin_rep:
                if bit == '0':
                    break
                x += 1
            if x == 0:
                continue
            if x == 1 or x > 4:
                return False
        else:
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False
    return x == 0


def validUTF8(data):
    x = 0
    if data is None:
        return False
    for number in data:
        if x == 0:
            if number & 128 == 0:
                x = 0
            elif number & 224 == 192:
                x = 1
            elif number & 240 == 224:
                x = 2
            elif number & 248 == 240:
                x = 3
            else:
                return False
        else:
            if number & 192 != 128:
                return False
    if x == 0:
        return True
    return False


def validUTF8_v4(data):
    byt = 0
    m1 = 1 << 7
    m2 = 1 << 6
    for number in data:
        mask = 1 << 7
        if byt == 0:
            while mask & number:
                byt += 1
                mask = mask >> 1

            if byt == 0:
                continue

            if byt == 1 or byt > 4:
                return False
        else:
            if not (number & m1 and not (number & m2)):
                return False
        byt -= 1
        return byt == 0
