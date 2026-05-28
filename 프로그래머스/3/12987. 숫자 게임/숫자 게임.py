from collections import deque

def solution(A, B):
    sorted_A = deque(sorted(A, reverse=True))
    sorted_B = deque(sorted(B, reverse=True))
    answer = 0
    while sorted_A and sorted_B:
        if sorted_A[0] < sorted_B[0]:
            answer += 1
            sorted_A.popleft()
            sorted_B.popleft()
        elif sorted_A[0] >= sorted_B[0]:
            sorted_A.popleft()
    return answer