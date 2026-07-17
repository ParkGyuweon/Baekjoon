def solution(answers):
    answer = []
    score = [0, 0, 0]
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for idx in range(len(answers)):
        if answers[idx] == first[idx % 5]:
            score[0] += 1
        if answers[idx] == second[idx % 8]:
            score[1] += 1
        if answers[idx] == third[idx % 10]:
            score[2] += 1
    if max(score) == score[0]:
        answer.append(1)
    if max(score) == score[1]:
        answer.append(2)
    if max(score) == score[2]:
        answer.append(3)
    return answer