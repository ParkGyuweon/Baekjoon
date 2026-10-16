from math import factorial

def solution(weights):
    answer = 0
    set_weights = sorted(list(set(weights)))
    cnt_list = [0] * 1001
    for weight in weights:
        cnt_list[weight] += 1
        
    for cnt in cnt_list:
        if cnt != 1 and cnt != 0:
            answer += factorial(cnt) // (factorial(2) * factorial (cnt - 2))
        
    for person1 in range(len(set_weights) - 1):
        for person2 in range(person1 + 1, len(set_weights)):
            if set_weights[person2] / set_weights[person1] in (1.0, 2.0, 4/3, 1.5):
                answer += cnt_list[set_weights[person1]] * cnt_list[set_weights[person2]]

    return answer