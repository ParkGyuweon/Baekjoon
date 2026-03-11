N, M, B = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
max_val = 0
min_val = 10E10
min_time = 10E10
min_height = 0

for y in range(N):
    max_val = max(max_val, max(grid[y]))
    min_val = min(min_val, min(grid[y]))

for height in range(max_val, min_val - 1, -1):
    cur_time, high_block, low_block = 0, 0, 0
    for y in range(N):
        for x in range(M):
            if grid[y][x] > height:
                high_block += grid[y][x] - height
            elif grid[y][x] < height:
                low_block += height - grid[y][x]

    if high_block + B < low_block:
        continue

    cur_time = high_block * 2 + low_block * 1
    if min_time == cur_time:
        continue
    min_time = min(min_time, cur_time)
    if min_time == cur_time:
        min_height = height

print(min_time, min_height)
