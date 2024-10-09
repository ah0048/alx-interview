#!/usr/bin/python3
""" lockboxes """


def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened'''
    if not boxes or len(boxes) == 0 or not isinstance(boxes, list):
        return False
    length = len(boxes)
    closed_boxes = list(range(1, length))
    for key in boxes[0]:
        if key < length and key in closed_boxes:  # Added key validation
            closed_boxes.remove(key)
            openBoxes(boxes, key,
                      closed_boxes, length)  # Added length parameter
    return len(closed_boxes) == 0


def openBoxes(boxes, key, closed_boxes, length):
    '''Opens the boxes'''
    for new_key in boxes[key]:
        if new_key < length and new_key in closed_boxes:
            closed_boxes.remove(new_key)
            openBoxes(boxes, new_key, closed_boxes, length)
