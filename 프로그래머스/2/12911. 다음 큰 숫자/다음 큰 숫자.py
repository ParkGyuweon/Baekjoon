def solution(n):
    cur_number = n + 1
    while bin(n)[2:].count('1') != bin(cur_number)[2:].count('1'):
        cur_number += 1
    answer = cur_number
    return answer