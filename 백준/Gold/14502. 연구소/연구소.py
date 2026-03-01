N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
virus = []
wall = []
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
max_val = 0

for y in range(N):
    for x in range(M):
        if grid[y][x] == 2:
            virus.append((x, y))
        elif grid[y][x] == 1:
            wall.append((x, y))

def bfs(grid, virus):
    stack = list(virus)
    visited = list(virus)
    while stack:
        cur_x, cur_y = stack.pop()
        for x, y in direction:
            new_x, new_y = cur_x + x, cur_y + y
            if 0 <= new_x < M and 0 <= new_y < N and grid[new_y][new_x] == 0 and (new_x, new_y) not in visited:
                stack.append((new_x, new_y))
                visited.append((new_x, new_y))
    return (N * M) - len(wall) - len(visited) - 3

def back(grid, wall_cnt):
    global max_val
    if wall_cnt == 3:
        cur = bfs(grid, virus)
        max_val = max(max_val, cur)
        return
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 0:
                grid[y][x] = 1
                back(grid, wall_cnt + 1)
                grid[y][x] = 0

back(grid, 0)
print(max_val)