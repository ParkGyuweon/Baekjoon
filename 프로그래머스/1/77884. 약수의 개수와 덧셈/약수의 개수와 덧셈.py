def solution(left, right):
    plus, minus = 0, 0
    for num in range(left, right + 1):
        divisor = 0
        for sec_num in range(1, num + 1):
            if num % sec_num == 0:
                divisor += 1
        if divisor % 2 == 0:
            plus += num
        else:
            minus += num
    return plus - minus