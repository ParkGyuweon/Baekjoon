def solution(lottos, win_nums):
    min_val, max_val = 7, 1
    for lotto in lottos:
        if lotto != 0 and lotto in win_nums:
            min_val -= 1
        if lotto != 0 and lotto not in win_nums:
            max_val += 1
    if min_val == 7:
        min_val = 6
    if max_val == 7:
        max_val = 6
    return [max_val, min_val]