def solution(num):
    turn = 0
    while num != 1 and turn <= 500:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        turn = turn + 1
    if num == 1:
        return turn
    else:
        return -1 