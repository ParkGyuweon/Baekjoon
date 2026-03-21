import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [[0] + list(map(int, input().split())) for _ in range(N)]

for y in range(N):
    for x in range(N):
        grid[y][x + 1] = grid[y][x] + grid[y][x + 1]

for x in range(N + 1):
    for y in range(N - 1):
        grid[y + 1][x] = grid[y][x] + grid[y + 1][x]
grid = [[0] * (N + 1)] + grid

for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    print(grid[y2][x2] - grid[y2][x1 - 1] - grid[y1 - 1][x2] + grid[y1 - 1][x1 - 1])
