from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
virus_possible = []
wall_cnt = 0
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
min_val = 10E10

for y in range(N):
    for x in range(N):
        if grid[y][x] == 2:
            virus_possible.append((x, y))
        elif grid[y][x] == 1:
            wall_cnt += 1

if len(virus_possible) + wall_cnt == N * N:
    print(0)
    exit()

def bfs(grid, virus):
    zero_cnt = 0
    virus_cnt = len(virus_possible)
    visited = [-1] * (N * N)
    stack = deque(virus)
    while stack:
        cur_x, cur_y, cur_time = stack.popleft()
        for x, y in direction:
            new_x, new_y = cur_x + x, cur_y + y
            if 0 <= new_x < N and 0 <= new_y < N and grid[new_y][new_x] != 1 and visited[new_y * N + new_x] == -1:
                if grid[new_y][new_x] == 0:
                    zero_cnt += 1
                stack.append((new_x, new_y, cur_time + 1))
                visited[new_y * N + new_x] = 0
                if zero_cnt + wall_cnt + virus_cnt == N * N:
                    return cur_time + 1

def back(grid, wall_cnt, virus, start, M, virus_possible):
    global min_val
    if len(virus) == M:
        cur = bfs(grid, virus)
        if cur != None:
            min_val = min(min_val, cur)
        return

    for idx in range(start, len(virus_possible)):
        virus.append((virus_possible[idx][0], virus_possible[idx][1], 0))
        back(grid, wall_cnt, virus, idx + 1, M, virus_possible)
        virus.pop()

back(grid, wall_cnt, [], 0, M, virus_possible)
if min_val == 10E10:
    print(-1)
else:
    print(min_val)