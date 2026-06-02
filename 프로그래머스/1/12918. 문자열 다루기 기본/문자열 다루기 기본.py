def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    for char in s:
        if not char.isnumeric():
            return False
    return True