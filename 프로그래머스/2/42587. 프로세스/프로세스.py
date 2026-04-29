from collections import deque
def solution(priorities, location):
    new_list = deque()
    for idx in range(len(priorities)):
        new_list.append((priorities[idx], idx))
    priority_list = [0 for _ in range(10)]
    for idx in range(len(priorities)):
        priority_list[priorities[idx]] += 1
    turn = 1
    while True:
        cur_work, cur_location = new_list.popleft()
        for idx in range(cur_work + 1, len(priority_list)):
            if priority_list[idx]:
                new_list.append((cur_work, cur_location))
                break
        else:
            if cur_location == location:
                return turn
            priority_list[cur_work] -= 1
            turn += 1