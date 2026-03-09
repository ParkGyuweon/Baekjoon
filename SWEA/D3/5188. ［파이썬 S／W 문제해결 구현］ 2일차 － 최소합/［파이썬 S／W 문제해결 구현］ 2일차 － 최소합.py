T = int(input())
direction = [(0, 1), (1, 0)]

def dfs(grid):
    global min_val
    stack = [(0, 0, grid[0][0])]
    while stack:
        cur_x, cur_y, cur_sum = stack.pop()
        for x, y in direction:
            new_x, new_y = cur_x + x, cur_y + y
            if new_x == N - 1 and new_y == N - 1:
                min_val = min(min_val, cur_sum + grid[new_y][new_x])
                break
            if 0 <= new_x < N and 0 <= new_y < N:
                stack.append((new_x, new_y, cur_sum + grid[new_y][new_x]))

for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    min_val = 10E10
    dfs(grid)
    print(f'#{t} {min_val}')