from collections import deque

def solution(people, limit):
    people.sort()
    people= deque(people)
    answer = 0
    while people:
        cur_max = people.pop()
        if people and people[0] + cur_max <= limit:
            people.popleft()
        answer += 1
    return answer