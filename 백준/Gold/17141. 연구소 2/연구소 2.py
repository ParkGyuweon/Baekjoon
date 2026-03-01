from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
virus_possible = []
wall = []
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
min_val = 10E10

for y in range(N):
    for x in range(N):
        if grid[y][x] == 2:
            virus_possible.append((x, y))
        elif grid[y][x] == 1:
            wall.append((x, y))

def bfs(grid, virus, virus_visited):
    zero_cnt = len(virus)
    stack = deque(virus)
    visited = [-1] * (N * N)
    if len(virus_visited) + len(wall) == N * N:
        return 0
    for x, y in virus_visited:
        visited[y * N + x] = 0
    while stack:
        cur_x, cur_y, cur_time = stack.popleft()
        for x, y in direction:
            new_x, new_y = cur_x + x, cur_y + y
            if 0 <= new_x < N and 0 <= new_y < N and grid[new_y][new_x] != 1 and (new_x, new_y, 0) not in virus and visited[new_y * N + new_x] == -1:
                stack.append((new_x, new_y, cur_time + 1))
                visited[new_y * N + new_x] = 0
                zero_cnt += 1
                if zero_cnt + len(wall) == N * N:
                    return cur_time + 1

def back(grid, wall, virus, virus_visited, start, M, virus_possible):
    global min_val
    if len(virus) == M:
        cur = bfs(grid, virus, virus_visited)
        if cur != None:
            min_val = min(min_val, cur)
        return

    for idx in range(start, len(virus_possible)):
        virus.append((virus_possible[idx][0], virus_possible[idx][1], 0))
        virus_visited.append(virus_possible[idx])
        back(grid, wall, virus, virus_visited, idx + 1, M, virus_possible)
        virus.pop()
        virus_visited.pop()

back(grid, wall, [], [], 0, M, virus_possible)
if min_val == 10E10:
    print(-1)
else:
    print(min_val)