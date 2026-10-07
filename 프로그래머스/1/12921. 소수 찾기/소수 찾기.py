def solution(n):
    answer = 0
    for num in range(2, n + 1):
        for div in range(2, int(num ** (1/2)) + 1):
            if num % div == 0:
                break
        else:
            answer += 1        
    return answer