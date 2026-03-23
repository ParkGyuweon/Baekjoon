grid = [[0 for _ in range(2001)] for _ in range(2001)]

x1, y1, x2, y2 = map(int, input().split())
for y in range(y1, y2):
    for x in range(x1, x2):
        grid[y + 1000][x + 1000] = 1
x1, y1, x2, y2 = map(int, input().split())
for y in range(y1, y2):
    for x in range(x1, x2):
        grid[y + 1000][x + 1000] = 1
x1, y1, x2, y2 = map(int, input().split())
for y in range(y1, y2):
    for x in range(x1, x2):
        grid[y + 1000][x + 1000] = 0

sum_val = 0
for y in range(2001):
    sum_val += sum(grid[y])
print(sum_val)