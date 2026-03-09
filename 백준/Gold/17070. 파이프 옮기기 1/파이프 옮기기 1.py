import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
pipe = {0: [(-1, 0)],
        1: [(0, -1)],
        2: [(-1, 0), (0, -1), (-1, -1)]} # 가로, 세로, 대각선
pipe_possible = [(0, 2), (1, 2), (0, 1, 2)] # 가로 세로 대각선일 때 가능한 경우의 수
number_grid = [[{} for _ in range(N)] for _ in range(N)]
total_case = 0

def dfs(grid, pipe, pipe_possible, cur_x, cur_y, cur_dir):
    if not (0 <= cur_x < N and 0 <= cur_y < N and grid[cur_y][cur_x] == 0):
        return 0

    if (cur_x == 1 and cur_y == 0 and cur_dir == 0):
        return 1

    if cur_dir in number_grid[cur_y][cur_x]:
        return number_grid[cur_y][cur_x][cur_dir]

    flag = False
    number_grid[cur_y][cur_x][cur_dir] = 0
    for x, y in pipe[cur_dir]:
        new_x, new_y = cur_x + x, cur_y + y
        if not(0 <= new_x < N and 0 <= new_y < N and grid[new_y][new_x] == 0):
            break
    else:
        flag = True
        for item in pipe_possible[cur_dir]:
            number_grid[cur_y][cur_x][cur_dir] += dfs(grid, pipe, pipe_possible, new_x, new_y, item)
    if not flag:
        return 0
    return number_grid[cur_y][cur_x][cur_dir]

print(dfs(grid, pipe, pipe_possible, N - 1, N - 1, 0) + dfs(grid, pipe, pipe_possible, N - 1, N - 1, 1) + dfs(grid, pipe, pipe_possible, N - 1, N - 1, 2))