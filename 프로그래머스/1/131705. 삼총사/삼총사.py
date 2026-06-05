def solution(number):
    answer = 0
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            for k in range(j + 1, len(number)):
                if number[k] + number[j] + number[i] == 0:
                    answer += 1
    return answer