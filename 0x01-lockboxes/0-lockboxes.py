#!/usr/bin/python3
""" lockboxes """


def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened'''
    if not boxes or len(boxes) == 0 or type(boxes) is not list:
        return False
    length = len(boxes)
    opened_boxes = {0}  # set
    for key in boxes[0]:
        if key not in opened_boxes:
            opened_boxes.add(key)
            openBoxes(boxes, key, opened_boxes)
    return len(opened_boxes) == length


def openBoxes(boxes, key, opened_boxes):
    '''Opens the boxes'''
    for new_key in boxes[key]:
        if new_key not in opened_boxes:
            opened_boxes.add(new_key)
            openBoxes(boxes, new_key, opened_boxes)
