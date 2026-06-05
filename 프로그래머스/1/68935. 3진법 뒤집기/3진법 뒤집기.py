def solution(n):
    third_number = ''
    while n != 0:
        third_number += str(n % 3)
        n = n // 3
    answer = 0
    third_number = third_number[::-1]
    for idx in range(len(third_number)):
        answer += int(third_number[idx]) * (3 ** idx)
        print()
    return answer