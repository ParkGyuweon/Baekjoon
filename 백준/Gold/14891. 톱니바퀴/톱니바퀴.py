from collections import deque

first = deque(map(int, list(input())))
second = deque(map(int, list(input())))
third = deque(map(int, list(input())))
fourth = deque(map(int, list(input())))
total = [first, second, third, fourth]
K = int(input()) # 회전 횟수
move = [list(map(int, input().split())) for _ in range(K)] # 톱니 번호, 회전 방향 (1이면 시계, -1이면 반시계)
opposite_direction = {1 : -1, -1 : 1}

for i in range(K):
    number, direction = move[i]
    cur_move = [(number - 1, direction)]
    left_idx, right_idx, left_direction, right_direction = number - 1, number - 1, direction, direction
    while left_idx >= 1 and total[left_idx][6] != total[left_idx - 1][2]:
        cur_move.append((left_idx - 1, opposite_direction[left_direction]))
        left_direction = opposite_direction[left_direction]
        left_idx -= 1
    while right_idx < 3 and total[right_idx][2] != total[right_idx + 1][6]:
        cur_move.append((right_idx + 1, opposite_direction[right_direction]))
        right_direction = opposite_direction[right_direction]
        right_idx += 1

    for item in cur_move:
        total[item[0]].rotate(item[1])

score = 0
for i in range(4):
    if total[i][0] == 1:
        score += 2 ** i
print(score)
