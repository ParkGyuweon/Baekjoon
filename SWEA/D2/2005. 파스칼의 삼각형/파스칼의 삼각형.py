T = int(input())

for t in range(1, T + 1):
    N = int(input())
    grid = [[0 for _ in range(2 * N + 1)] for _ in range(N)]
    for y in range(N):
        if y == 0:
            grid[y][N] = 1
        else:
            for x in range(N - y, N + y + 1):
                grid[y][x] = grid[y - 1][x - 1] + grid[y - 1][x + 1]

    print(f'#{t}')
    for y in range(N):
        for x in range(2 * N + 1):
            if grid[y][x] != 0:
                print(grid[y][x], end = ' ')
        print()