from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for y in range(N):
    for x in range(M):
        if grid[y][x] == 2:
            start_x, start_y = x, y
            grid[y][x] = 0
        elif grid[y][x] == 1:
            grid[y][x] = -1

stack = deque([(start_x, start_y)])
while stack:
    cur_x, cur_y = stack.popleft()
    for x, y in direction:
        new_x, new_y = cur_x + x, cur_y + y
        if 0 <= new_x < M and 0 <= new_y < N and grid[new_y][new_x] == -1:
            grid[new_y][new_x] = grid[cur_y][cur_x] + 1
            stack.append((new_x, new_y))
for y in range(N):
    print(' '.join(map(str, grid[y])))