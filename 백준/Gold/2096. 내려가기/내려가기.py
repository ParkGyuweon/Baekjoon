import sys
input = sys.stdin.readline

N = int(input().strip())
direction = [(0, 1), (1, 1), (-1, 1)]
grid = list(map(int, input().split()))
cur_max = grid[:]
cur_min = grid[:]
min_val, max_val, y_idx = 10E10, 0, 1

while y_idx <= N - 1:
    new_max, new_min = [0] * 3, [0] * 3
    cur_grid = list(map(int, input().split()))
    new_max[0] = cur_grid[0] + max(cur_max[0], cur_max[1])
    new_max[1] = cur_grid[1] + max(cur_max[0], cur_max[1], cur_max[2])
    new_max[2] = cur_grid[2] + max(cur_max[1], cur_max[2])

    new_min[0] = cur_grid[0] + min(cur_min[0], cur_min[1])
    new_min[1] = cur_grid[1] + min(cur_min[0], cur_min[1], cur_min[2])
    new_min[2] = cur_grid[2] + min(cur_min[1], cur_min[2])

    y_idx += 1
    cur_max, cur_min = new_max, new_min

print(max(cur_max), min(cur_min))