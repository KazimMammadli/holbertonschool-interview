#!/usr/bin/python3
"""This module defines whether all boxes have keys."""


def canUnlockAll(boxes):
    """Return true if all boxes have keys."""
    flag = 0
    length = len(boxes)
    for i in range(1, length):
        for j in range(length):
            if i in boxes[j] and i != j:
                flag = 1
        if flag == 0:
            return False
    return True
