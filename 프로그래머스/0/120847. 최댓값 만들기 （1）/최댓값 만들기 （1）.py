def solution(numbers):
    answer = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if answer < numbers[i] * numbers[j]:
                answer = numbers[i] * numbers[j]
    return answer