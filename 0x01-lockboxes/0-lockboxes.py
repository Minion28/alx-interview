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
