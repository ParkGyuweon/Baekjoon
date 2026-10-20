from collections import deque

def solution(food):
    answer = deque([0])
    for idx in range(len(food) - 1, 0, -1):
        for i in range(food[idx] // 2):
            answer.append(idx)
            answer.appendleft(idx)
    return ''.join(map(str, answer))