def solution(n):
    fibonnachi = [0] * (n + 1)
    fibonnachi[0], fibonnachi[1], fibonnachi[2] = 0, 1, 1
    for idx in range(2, n + 1):
        fibonnachi[idx] = fibonnachi[idx - 1] + fibonnachi[idx - 2]
    answer = fibonnachi[n] % 1234567
    return answer