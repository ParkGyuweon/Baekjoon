N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
rotation = [list(map(int, input().split())) for _ in range(K)]
total_list = []
min_val = 10E10

def change_grid(grid, item):
    for line in range(item[2], 0, -1):
        start_x, start_y, end_x, end_y = item[1] -1 - line, item[0] -1 - line, item[1] - 1 + line, item[0] - 1 + line
        UR_temp = grid[start_y][end_x]
        for x in range(end_x - 1, start_x - 1, -1):
            grid[start_y][x + 1] = grid[start_y][x]
        DR_temp = grid[end_y][end_x]
        for y in range(end_y - 1, start_y - 1, -1):
            grid[y + 1][end_x] = grid[y][end_x]
        DL_temp = grid[end_y][start_x]
        for x in range(start_x + 1, end_x):
            grid[end_y][x - 1] = grid[end_y][x]
        UL_temp = grid[start_y][start_x]
        for y in range(start_y + 1, end_y):
            grid[y - 1][start_x] = grid[y][start_x]
        grid[start_y + 1][end_x] = UR_temp
        grid[end_y][end_x - 1] = DR_temp
        grid[end_y - 1][start_x] = DL_temp
        grid[start_y][start_x + 1] = UL_temp

def choice(K, current, grid):
    global min_val
    if len(current) == K:
        cur_min = 10E10
        for y in range(N):
            cur_min = min(cur_min, sum(grid[y]))
        min_val = min(min_val, cur_min)
        return
    for item in range(K):
        if item in current:
            continue
        current.append(item)
        new_grid = [grid[i][:] for i in range(N)]
        change_grid(new_grid, rotation[item])
        choice(K, current, new_grid)
        current.pop()

choice(K, [], grid)
print(min_val)