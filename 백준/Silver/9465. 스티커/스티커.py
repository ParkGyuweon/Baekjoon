T = int(input())

for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(2)]

    for item in range(N):
        if item == 0:
            continue
        if item == 1:
            grid[0][item] += grid[1][item - 1]
            grid[1][item] += grid[0][item - 1]
            continue
        grid[0][item] = grid[0][item] + max(grid[1][item - 1], grid[0][item - 2], grid[1][item - 2])
        grid[1][item] = grid[1][item] + max(grid[0][item - 1], grid[0][item - 2], grid[1][item - 2])

    print(max(max(grid[1]), max(grid[0])))