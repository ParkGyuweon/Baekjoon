T = int(input())
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
command_direction = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
direction_picture = {0: '^', 1: '>', 2: 'v', 3: '<'}
for t in range(1, T + 1):
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    N = int(input())
    commands = list(input())

    for y in range(H):
        for x in range(W):
            if grid[y][x] == '^':
                cur_x, cur_y, cur_direction = x, y, 0
            elif grid[y][x] == 'v':
                cur_x, cur_y, cur_direction = x, y, 2
            elif grid[y][x] == '>':
                cur_x, cur_y, cur_direction = x, y, 1
            elif grid[y][x] == '<':
                cur_x, cur_y, cur_direction = x, y, 3

    for character in commands:
        if character in ('U', 'R', 'D', 'L'):
            cur_direction = command_direction[character]
            new_x, new_y = cur_x + direction[cur_direction][0], cur_y + direction[cur_direction][1]
            if 0 <= new_x < W and 0 <= new_y < H and grid[new_y][new_x] == '.':
                grid[cur_y][cur_x] = '.'
                cur_x, cur_y = new_x, new_y
            grid[cur_y][cur_x] = direction_picture[cur_direction]
        else:
            if cur_direction == 0:
                for y in range(cur_y, -1, -1):
                    if grid[y][cur_x] in ('*', '#'):
                        if grid[y][cur_x] == '*':
                            grid[y][cur_x] = '.'
                        break
            elif cur_direction == 1:
                for x in range(cur_x, W):
                    if grid[cur_y][x] in ('*', '#'):
                        if grid[cur_y][x] == '*':
                            grid[cur_y][x] = '.'
                        break
            elif cur_direction == 2:
                for y in range(cur_y, H):
                    if grid[y][cur_x] in ('*', '#'):
                        if grid[y][cur_x] == '*':
                            grid[y][cur_x] = '.'
                        break
            elif cur_direction == 3:
                for x in range(cur_x, -1, -1):
                    if grid[cur_y][x] in ('*', '#'):
                        if grid[cur_y][x] == '*':
                            grid[cur_y][x] = '.'
                        break

    print(f'#{t}', end=' ')
    for item in grid:
        print(''.join(item))