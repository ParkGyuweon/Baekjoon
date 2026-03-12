T = int(input())
direction = {1: [('D', 'R', 'L', 'U'), (0, 1, 'D'), (0, -1, 'U'), (1, 0, 'R'), (-1, 0, 'L')],
             2: [('U', 'D'), (0, 1, 'D'), (0, -1, 'U')],
             3: [('L', 'R'), (-1, 0, 'L'), (1, 0, 'R')],
             4: [('D', 'L'), (0, -1, 'U'), (1, 0, 'R')],
             5: [('L', 'U'), (1, 0, 'R'), (0, 1, 'D')],
             6: [('R', 'U'), (-1, 0, 'L'), (0, 1, 'D')],
             7: [('R', 'D'), (-1, 0, 'L'), (0, -1, 'U')],
             0: []}
direction_conversion = {'D': 'U', 'U': 'D', 'L': 'R', 'R': 'L', 0: 0}

def pipe(grid, start_x, start_y):
    stack = [(start_x, start_y, 0, 0)]
    while stack:
        cur_x, cur_y, cur_dir, cur_time = stack.pop(0)
        if cur_time + 1 >= L:
            continue
        for item in direction[grid[cur_y][cur_x]][1:]:
            new_x, new_y = cur_x + item[0], cur_y + item[1]
            if 0 <= new_x < M and 0 <= new_y < N and grid[new_y][new_x] != 0 and item[2] != direction_conversion[cur_dir] and item[2] in direction[grid[new_y][new_x]][0] and (new_x, new_y) not in total_set:
                stack.append((new_x, new_y, item[2], cur_time + 1))
                total_set.add((new_x, new_y))

for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    total_set = {(C, R)}
    pipe(grid, C, R)
    print(f'#{t} {len(total_set)}')