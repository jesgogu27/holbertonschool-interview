#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1
    and each box may contain keys to the other boxes.
    """
    keys = [0]
    for b in keys:
        for key in boxes[b]:
            if key not in keys:
                if key < len(boxes):
                    keys.append(key)

    if len(keys) == len(boxes):
        return True
    return False
