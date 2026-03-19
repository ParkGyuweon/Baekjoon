from collections import deque

M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

mature_tomato = deque()
for y in range(N):
    for x in range(M):
        if grid[y][x] == 1:
            mature_tomato.append((x, y, 0))
while mature_tomato:
    cur_x, cur_y, cur_day = mature_tomato.popleft()
    for x, y in direction:
        new_x, new_y = cur_x + x, cur_y + y
        if 0 <= new_x < M and 0 <= new_y < N and grid[new_y][new_x] == 0:
            mature_tomato.append((new_x, new_y, cur_day + 1))
            grid[new_y][new_x] = 1

sum_val = 0
for y in range(N):
    if 0 in grid[y]:
        print(-1)
        break
else:
    print(cur_day)