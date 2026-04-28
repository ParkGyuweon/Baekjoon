from collections import defaultdict

def solution(clothes):
    global answer
    clothes_kind = defaultdict(list)
    for name, kind in clothes:
        clothes_kind[kind].append(name)
        
    answer = 1
    for key, value in clothes_kind.items():
        answer *= (len(value) + 1)
    return answer - 1