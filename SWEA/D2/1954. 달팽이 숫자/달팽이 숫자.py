T = int(input())
for t in range(1, T + 1):
    N = int(input())
    print(f'#{t}')
    if N == 1:
        print(1)
    else:
        dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
        x, y, direction = 0, 0, 0
        grid = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(1, N * N + 1):
            grid[y][x] = i
            new_x, new_y = x + dx[direction], y + dy[direction]
            if grid[new_y][new_x] != 0:
                direction = (direction + 1) % 4
                new_x, new_y = x + dx[direction], y + dy[direction]
            elif (new_x == 0 or new_x == N - 1) and (new_y == 0 or new_y == N - 1):
                direction = (direction + 1) % 4
            x, y = new_x, new_y
        for i in range(N):
            print(' '.join(map(str, grid[i])))

