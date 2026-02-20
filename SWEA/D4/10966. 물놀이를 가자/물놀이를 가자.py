from collections import deque
 
T = int(input())
 
def bfs(N, M, visited, stack, direction):
    while stack:
        cur_x, cur_y = stack.popleft()
        for i in range(4):
            new_x, new_y = cur_x + direction[i][0], cur_y + direction[i][1]
            if 0 <= new_x < M and 0 <= new_y < N and visited[new_y * M + new_x] == -1:
                visited[new_y * M + new_x] = visited[cur_y * M + cur_x] + 1
                stack.append((new_x, new_y))
            else:
                continue
 
for t in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(input()) for _ in range(N)]
    visited = [-1 for _ in range(N * M)]
    stack = deque()
    for y in range(N):
        for x in range(M):
            if grid[y][x] == 'W':
                stack.append((x, y))
                visited[M * y + x] = 0
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    bfs(N, M, visited, stack, direction)
    print(f'#{t} {sum(visited)}')