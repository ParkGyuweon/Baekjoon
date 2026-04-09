from collections import deque
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    visited = [[0 for _ in range(N)] for _ in range(N)]
    grid = [list(map(int, input().split())) for _ in range(N)]

    stack = deque([(0, 0)])
    while stack:
        cur_x, cur_y = stack.popleft()
        for x, y in direction:
            new_x, new_y = cur_x + x, cur_y + y
            if 0 <= new_x < N and 0 <= new_y < N:
                if grid[new_y][new_x] > grid[cur_y][cur_x]:
                   if visited[new_y][new_x] == 0 or (visited[new_y][new_x] > visited[cur_y][cur_x] + grid[new_y][new_x] - grid[cur_y][cur_x] + 1):
                       visited[new_y][new_x] = visited[cur_y][cur_x] + 1 + (grid[new_y][new_x] - grid[cur_y][cur_x])
                       stack.append((new_x, new_y))
                else:
                    if visited[new_y][new_x] == 0 or visited[new_y][new_x] > visited[cur_y][cur_x] + 1:
                        visited[new_y][new_x] = visited[cur_y][cur_x] + 1
                        stack.append((new_x, new_y))
    print(f'#{t} {visited[N - 1][N - 1]}')