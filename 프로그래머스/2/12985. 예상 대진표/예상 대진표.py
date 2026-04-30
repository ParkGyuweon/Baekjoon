from collections import deque

def solution(n,a,b):
    answer = 0
    member_list = deque([i + 1 for i in range(n)])
    new_list = deque()
    turn = 1
    while len(member_list) >= 2:
        person_1 = member_list.popleft()
        person_2 = member_list.popleft()
        if (person_1 == a and person_2 == b) or (person_1 == b and person_2 == a):
            return turn
        if person_1 in (a, b):
            new_list.append(person_1)
        elif person_2 in (a, b):
            new_list.append(person_2)
        else:
            new_list.append(person_1)
        if len(new_list) == n // 2 ** turn:
            turn += 1
            member_list = deque(new_list)
            new_list = deque()
            