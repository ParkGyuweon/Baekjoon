def solution(n):
    answer = ''
    turn = 0
    while turn != n:
        if turn % 2 == 0:
            answer += '수'
        else:
            answer += '박'
        turn += 1
    return answer