def solution(n):
    answer = 0
    fibonnachi_list = [0] * (n + 3)
    fibonnachi_list[0], fibonnachi_list[1], fibonnachi_list[2] = 0, 1, 2
    for idx in range(3, n + 1):
        fibonnachi_list[idx] = fibonnachi_list[idx - 1] + fibonnachi_list[idx - 2]
        
    answer = fibonnachi_list[n]

    return answer % 1234567