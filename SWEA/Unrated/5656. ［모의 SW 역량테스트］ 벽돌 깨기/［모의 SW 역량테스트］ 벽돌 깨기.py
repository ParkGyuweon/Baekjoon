T = int(input())
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def marble(grid, boom_cnt, eliminate_block):
    global min_val
    if boom_cnt == N:
        min_val = min(min_val, total_block - eliminate_block)
        return

    for x in range(W):
        for y in range(H):
            if grid[y][x] != 0:
                new_grid = [grid[i][:] for i in range(H)]
                new_grid, block = boom_bfs(new_grid, x, y)
                marble(new_grid, boom_cnt + 1, eliminate_block + block)
                break
        else:
            continue

def boom_bfs(grid, start_x, start_y):
    stack = [(start_x, start_y, grid[start_y][start_x])]
    grid[start_y][start_x] = 0
    block = 1
    while stack:
        cur_x, cur_y, cur_boom = stack.pop(0)
        for x, y in direction:
            for dist in range(1, cur_boom):
                new_x, new_y = cur_x + (x * dist), cur_y + (y * dist)
                if 0 <= new_x < W and 0 <= new_y < H and grid[new_y][new_x] != 0:
                    stack.append((new_x, new_y, grid[new_y][new_x]))
                    grid[new_y][new_x] = 0
                    block += 1
    for x in range(W):
        temp = [0] * H
        idx = H - 1
        for y in range(H - 1, -1, -1):
            if grid[y][x] != 0:
                temp[idx] = grid[y][x]
                idx -= 1
        for y in range(H -1, -1, -1):
            grid[y][x] = temp[y]

    return grid, block

for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]
    total_block = 0
    for y in range(H):
        for x in range(W):
            if grid[y][x] != 0:
                total_block += 1

    min_val = 10E10

    marble(grid, 0, 0)
    if min_val == 10E10:
        print(f'#{t} 0')
    else:
        print(f'#{t} {min_val}')