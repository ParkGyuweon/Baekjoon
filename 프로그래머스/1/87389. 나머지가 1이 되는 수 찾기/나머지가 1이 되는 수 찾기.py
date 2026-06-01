def solution(n):
    for num in range(1, n + 2):
        if n % num == 1:
            return num