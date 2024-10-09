#!/usr/bin/python3
""" lockboxes """


def canUnlockAll(boxes):
    '''Determines if all the boxes can be opened'''
    if not boxes or len(boxes) == 0 or not isinstance(boxes, list):
        return False
    length = len(boxes)
    closed_boxes = set(range(1, length))  # Use a set to track closed boxes
    open_boxes = set([0])  # Track opened boxes
    for key in boxes[0]:
        if key in closed_boxes and 0 <= key < length:  # Check if key is valid
            closed_boxes.remove(key)
            openBoxes(boxes, key, closed_boxes, open_boxes)
    return len(closed_boxes) == 0


def openBoxes(boxes, key, closed_boxes, open_boxes):
    '''Opens the boxes recursively'''
    for new_key in boxes[key]:
        if new_key in closed_boxes and new_key not in open_boxes and 0 <= new_key < len(boxes):
            closed_boxes.remove(new_key)
            open_boxes.add(new_key)  # Mark as opened
            openBoxes(boxes, new_key, closed_boxes, open_boxes)
