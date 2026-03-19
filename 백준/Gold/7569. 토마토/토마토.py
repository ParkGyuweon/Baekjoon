from collections import deque

M, N, H = map(int, input().split())
grid = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
direction = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (-1, 0, 0), (1, 0, 0)]

mature_tomato = deque()
for height in range(H):
    for y in range(N):
        for x in range(M):
            if grid[height][y][x] == 1:
                mature_tomato.append((height, x, y, 0))
while mature_tomato:
    cur_h, cur_x, cur_y, cur_day = mature_tomato.popleft()
    for h, x, y in direction:
        new_h, new_x, new_y = cur_h + h, cur_x + x, cur_y + y
        if 0 <= new_h < H and 0 <= new_x < M and 0 <= new_y < N and grid[new_h][new_y][new_x] == 0:
            mature_tomato.append((new_h, new_x, new_y, cur_day + 1))
            grid[new_h][new_y][new_x] = 1

sum_val = 0
for h in range(H):
    for y in range(N):
        if 0 in grid[h][y]:
            print(-1)
            exit()
print(cur_day)