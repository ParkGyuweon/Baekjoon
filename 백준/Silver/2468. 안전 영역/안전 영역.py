from collections import deque
N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
min_val, max_val = 100, 0
max_space = 0
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for y in range(N):
    for x in range(N):
        min_val = min(min_val, grid[y][x])
        max_val = max(max_val, grid[y][x])

for height in range(max_val + 1):
    new_grid = [[0 for _ in range(N)] for _ in range(N)]
    checked = [[0 for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if grid[y][x] <= height:
                new_grid[y][x] = 1
                checked[y][x] = 1

    cur_space = 0
    for y in range(N):
        for x in range(N):
            if new_grid[y][x] == 0 and checked[y][x] == 0:
                stack = deque([(x, y)])
                checked[y][x] = 1
                while stack:
                    cur_x, cur_y = stack.popleft()
                    for add_x, add_y in direction:
                        new_x, new_y = cur_x + add_x, cur_y + add_y
                        if 0 <= new_x < N and 0 <= new_y < N and new_grid[new_y][new_x] == 0 and checked[new_y][new_x] == 0:
                            stack.append((new_x, new_y))
                            checked[new_y][new_x] = 1
                cur_space += 1
    max_space = max(max_space, cur_space)

print(max_space)