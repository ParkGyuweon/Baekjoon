import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, list(input().strip()))) for _ in range(N)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[0 for _ in range(M)] for _ in range(N)]
block_visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1
stack = deque([(0, 0, 1, False)])
if N == 1 and M == 1:
    print(1)
else:
    while stack:
        cur_x, cur_y, cur_dist, cur_wall_flag = stack.popleft()
        for x, y in direction:
            new_x, new_y = cur_x + x, cur_y + y
            if 0 <= new_x < M and 0 <= new_y < N:
                if not cur_wall_flag and grid[new_y][new_x] == 0 and visited[new_y][new_x] == 0:
                    if new_x == M - 1 and new_y == N - 1:
                        print(cur_dist + 1)
                        exit()
                    else:
                        visited[new_y][new_x] = 1
                        stack.append((new_x, new_y, cur_dist + 1, False))
                elif not cur_wall_flag and grid[new_y][new_x] == 1 and block_visited[new_y][new_x] == 0:
                    if new_x == M - 1 and new_y == N - 1:
                        print(cur_dist + 1)
                        exit()
                    else:
                        block_visited[new_y][new_x] = 1
                        stack.append((new_x, new_y, cur_dist + 1, True))
                elif cur_wall_flag and grid[new_y][new_x] == 0 and block_visited[new_y][new_x] == 0:
                    if new_x == M - 1 and new_y == N - 1:
                        print(cur_dist + 1)
                        exit()
                    else:
                        block_visited[new_y][new_x] = 1
                        stack.append((new_x, new_y, cur_dist + 1, True))

    print(-1)