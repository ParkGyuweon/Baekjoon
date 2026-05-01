def solution(topping):
    answer = 0
    second_list = [0] * (max(topping) + 1)
    for item in topping:
        second_list[item] += 1
    first_list = [0] * (max(topping) + 1)
    first_zero = len(set(topping))
    second_zero = 0
    
    for cut_idx in range(0, len(topping)):
        second_list[topping[cut_idx]] -= 1
        first_list[topping[cut_idx]] += 1
        if first_list[topping[cut_idx]] == 1:
            first_zero -= 1
        if second_list[topping[cut_idx]] == 0:
            second_zero += 1
        if first_zero == second_zero:
            answer += 1
    return answer