N, M = map(int, input().split())
start_y, start_x, start_dir = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
direction = {0 : (0, -1), 1 : (1, 0), 2 : (0, 1), 3 : (-1, 0)}
around = [(0, 1), (0, -1), (1, 0), (-1, 0)]
clean_space = 0

def bfs(grid, start_x, start_y, start_dir):
    global clean_space
    stack = [(start_x, start_y, start_dir)]
    visited = [(start_x, start_y)]
    while stack:
        cur_x, cur_y, cur_dir = stack.pop(0)
        if grid[cur_y][cur_x] == 0:
            clean_space += 1
            grid[cur_y][cur_x] = 2
        need_clean = []
        for x, y in around:
            new_x, new_y = cur_x + x, cur_y + y
            if 0 <= new_x < M and 0 <= new_y < N and grid[new_y][new_x] == 0:
                need_clean.append((new_x, new_y))
        if not need_clean:
            new_x, new_y = cur_x + direction[(cur_dir + 2) % 4][0], cur_y + direction[(cur_dir + 2) % 4][1]
            if 0 <= new_x < M and 0 <= new_y < N and grid[new_y][new_x] != 1:
                stack.append((new_x, new_y, cur_dir))
            else:
                break
        else:
            cur_dir = (cur_dir + 3) % 4
            new_x, new_y = cur_x + direction[cur_dir][0], cur_y + direction[cur_dir][1]
            if 0 <= new_x < M and 0 <= new_y < N and grid[new_y][new_x] == 0:
                stack.append((new_x, new_y, cur_dir))
            else:
                stack.append((cur_x, cur_y, cur_dir))

bfs(grid, start_x, start_y, start_dir)
print(clean_space)