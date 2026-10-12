def solution(number, limit, power):
    cur_steel = 1
    for person in range(2, number + 1):
        cur_ability = 0
        for num in range(1, int(person ** 0.5) + 1):
            if person % num == 0:
                if num ** 2 != person:
                    cur_ability += 2
                else:
                    cur_ability += 1
        
        if cur_ability > limit:
            cur_steel += power
        else:
            cur_steel += cur_ability
        
    return cur_steel