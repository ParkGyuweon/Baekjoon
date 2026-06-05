def solution(d, budget):
    d.sort()
    cur_budget = 0
    turn = 0
    for num in d:
        if cur_budget + num > budget:
            break
        else:
            cur_budget += num
            turn += 1
    return turn