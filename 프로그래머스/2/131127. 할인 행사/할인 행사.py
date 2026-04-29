from collections import defaultdict

def solution(want, number, discount):
    want_set = set(want)
    want_dict = {}
    can_dict = {}
    answer = 0
    for item in range(len(want)):
        want_dict[want[item]] = number[item]
        can_dict[want[item]] = 0
    for idx in range(sum(number)):
        if discount[idx] in want_dict:
            can_dict[discount[idx]] += 1
    if can_dict == want_dict:
        answer += 1
            
    for idx in range(sum(number), len(discount)):
        if discount[idx - sum(number)] in want_set:
            can_dict[discount[idx - sum(number)]] -= 1
        if discount[idx] in want_set:
            can_dict[discount[idx]] += 1
        if can_dict == want_dict:
            answer += 1
            
    return answer