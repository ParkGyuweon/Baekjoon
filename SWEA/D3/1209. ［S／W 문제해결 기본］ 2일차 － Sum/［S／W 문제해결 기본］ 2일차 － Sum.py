for t in range(10):
    T = int(input())
    max_val = 0
    grid = [list(map(int, input().split())) for _ in range(100)]

    for row in grid:
        if sum(row) > max_val:
            max_val = sum(row)
    for col in list(zip(*grid)):
        if sum(col) > max_val:
            max_val = sum(col)

    cross1, cross2, height = 0, 99, 0
    cross1_sum, cross2_sum = 0, 0
    while height <= 99:
        cross1_sum = cross1_sum + grid[height][cross1]
        cross2_sum = cross2_sum + grid[height][cross2]
        height = height + 1
        cross1 = cross1 + 1
        cross2 = cross2 - 1
    if cross1_sum > max_val:
        max_val = cross1_sum
    if cross2_sum > max_val:
        max_val = cross2_sum
    print(f'#{T} {max_val}')