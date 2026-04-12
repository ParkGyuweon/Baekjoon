T = int(input())

def core_back(current, cur_line, idx, grid):
    global cur_max
    if idx == len(core_list):
        core_line[len(current)] = min(core_line[len(current)], cur_line)
        cur_max = len(current)
        return

    if len(core_list) - idx + len(current) < cur_max:
        return

    core_back(current, cur_line, idx + 1, grid)

    cur_y = [grid[y][core_list[idx][0]] for y in range(N)]
    cur_x = grid[core_list[idx][1]][:]

    for y in range(core_list[idx][1]):
        if grid[y][core_list[idx][0]] == 1:
            break
    else:
        cnt = 0
        for y in range(core_list[idx][1]):
            grid[y][core_list[idx][0]] = 1
            cnt += 1
        core_back(current + [core_list[idx]], cur_line + cnt, idx + 1, grid)
        for y in range(core_list[idx][1]):
            grid[y][core_list[idx][0]] = cur_y[y]
    for y in range(core_list[idx][1] + 1, N):
        if grid[y][core_list[idx][0]] == 1:
            break
    else:
        cnt = 0
        for y in range(core_list[idx][1] + 1, N):
            grid[y][core_list[idx][0]] = 1
            cnt += 1
        core_back(current + [core_list[idx]], cur_line + cnt, idx + 1, grid)
        for y in range(core_list[idx][1] + 1, N):
            grid[y][core_list[idx][0]] = cur_y[y]
    for x in range(core_list[idx][0]):
        if grid[core_list[idx][1]][x] == 1:
            break
    else:
        cnt = 0
        for x in range(core_list[idx][0]):
            grid[core_list[idx][1]][x] = 1
            cnt += 1
        core_back(current + [core_list[idx]], cur_line + cnt, idx + 1, grid)
        for x in range(core_list[idx][0]):
            grid[core_list[idx][1]][x] = cur_x[x]
    for x in range(core_list[idx][0] + 1, N):
        if grid[core_list[idx][1]][x] == 1:
            break
    else:
        cnt = 0
        for x in range(core_list[idx][0] + 1, N):
            grid[core_list[idx][1]][x] = 1
            cnt += 1
        core_back(current + [core_list[idx]], cur_line + cnt, idx + 1, grid)
        for x in range(core_list[idx][0] + 1, N):
            grid[core_list[idx][1]][x] = cur_x[x]


for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    core_list = []
    core_up, core_down, core_left, core_right = [], [], [], []
    cur_max = 0
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 1:
                core_list.append((x, y))

    core_line = [10E10] * (len(core_list) + 1)
    core_back([], 0, 0, grid)
    for idx in range(len(core_line) - 1, -1, -1):
        if core_line[idx] != 10E10:
           print(f'#{t} {core_line[idx]}')
           break
