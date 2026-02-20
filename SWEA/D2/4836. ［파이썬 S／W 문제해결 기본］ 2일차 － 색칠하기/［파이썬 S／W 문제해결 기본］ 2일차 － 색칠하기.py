T = int(input())
for t in range(1, T + 1):
    N = int(input())
    grid = [[0 for _ in range(10)] for _ in range(10)]

    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for y in range(r1, r2 + 1):
            for x in range(c1, c2 + 1):
                if grid[y][x] == 0:
                    grid[y][x] = color
                elif grid[y][x] == 1 and color == 2:
                    grid[y][x] = 3
                elif grid[y][x] == 2 and color == 1:
                    grid[y][x] = 3

    result = 0
    for y in range(10):
        result = result + grid[y].count(3)

    print(f'#{t} {result}')