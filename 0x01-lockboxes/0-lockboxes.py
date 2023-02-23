#!/usr/bin/python3
'''
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
'''


def canUnlockAll(boxes):
    unlock = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlock and key != box_id:
                unlock.append(key)
    if len(unlock) == len(boxes):
        return True
    return False
