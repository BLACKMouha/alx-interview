#!/usr/bin/python3

'''0-lockboxes module'''


def canUnlockAll(boxes):
    '''
    INIT visted_boxes = [False] * n
    TRAVERSE boxes:
        TRAVERSE box:
            IF visited_boxes[index] IS False
                MAKE VISITED box AT index True
    IF visited_boxes HOLDS ONLY True
        RETURN True
    ELSE
        RETURN False
    '''

    visited_boxes = [False] * len(boxes)
    visited_boxes[0] = True
    for box in boxes:
        for index in box:
            if visited_boxes[index] is False and index != boxes.index(box):
                visited_boxes[index] = True

    return all(visited_boxes)
