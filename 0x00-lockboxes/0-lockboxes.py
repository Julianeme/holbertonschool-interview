#!/usr/bin/python3
""" algorithm to solve the lockboxes problem"""


def canUnlockAll(boxes):
    """
    Return True if all boxes can be opened, False otherwise.
    """
    keys_found = {}
    answer = True
    i = 0
    while (i < len(boxes)):
        keys_found[i] = boxes[i]
        i += 1

    for box_key in range(1, len(boxes)):
        for i in range(0, len(boxes)):
            if (box_key in keys_found[i] and box_key != i):
                break
            elif (box_key not in keys_found[i] and i == len(boxes) - 1):
                answer = False
                return (answer)
    return answer
