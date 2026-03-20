from collections import deque
import sys
input = sys.stdin.readline

N = int(input().strip())
grid = [list(input().strip()) for _ in range(N)]
total_num, partial_num = 0, 0
total_checked = [[0 for _ in range(N)] for _ in range(N)]
partial_checked = [[0 for _ in range(N)] for _ in range(N)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for y in range(N):
    for x in range(N):
        if grid[y][x] == 'B':
            partial_checked[y][x] = 1

for y in range(N):
    for x in range(N):
        if total_checked[y][x] == 0:
            total_checked[y][x] = 1
            total_stack = deque([(x, y)])
            while total_stack:
                cur_x, cur_y = total_stack.popleft()
                for add_x, add_y in direction:
                    new_x, new_y = add_x + cur_x, add_y + cur_y
                    if 0 <= new_x < N and 0 <= new_y < N and grid[new_y][new_x] == grid[cur_y][cur_x] and total_checked[new_y][new_x] == 0:
                        total_checked[new_y][new_x] = 1
                        total_stack.append((new_x, new_y))
            total_num += 1
            if grid[y][x] == 'B':
                partial_num += 1
            elif grid[y][x] in ('R', 'G') and partial_checked[y][x] == 0:
                partial_stack = deque([(x, y)])
                while partial_stack:
                    cur_x, cur_y = partial_stack.popleft()
                    for add_x, add_y in direction:
                        new_x, new_y = add_x + cur_x, add_y + cur_y
                        if 0 <= new_x < N and 0 <= new_y < N and grid[new_y][new_x] != 'B' and partial_checked[new_y][new_x] == 0:
                            partial_checked[new_y][new_x] = 1
                            partial_stack.append((new_x, new_y))
                partial_num += 1

print(total_num, partial_num)