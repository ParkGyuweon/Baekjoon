def solution(n):
    answer = 0
    for start_num in range(1, n + 1):
        cur_number = start_num
        add_number = start_num + 1
        while cur_number < n:
            cur_number += add_number
            add_number += 1
        if cur_number == n:
            answer += 1
    return answer