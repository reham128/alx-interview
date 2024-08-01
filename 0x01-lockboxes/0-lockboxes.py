#!/usr/bin/python3
"""
A method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    - boxes is a list of lists
    - A key with the same number as a box opens that box
    - You can assume all keys will be positive integers
        - There can be keys that do not have boxes
    - The first box boxes[0] is unlocked
    - Return True if all boxes can be opened, else return False
    """
    n = len(boxes)
    opened_boxes = set([0])
    keys = set(boxes[0])

    while keys:
        new_keys = set()
        for key in keys:
            if key not in opened_boxes and key < n:
                opened_boxes.add(key)
                new_keys.update(boxes[key])
        if not new_keys:
            break
        keys = new_keys

    return len(opened_boxes) == n
