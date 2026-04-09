from collections import deque
T = int(input())
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, list(input()))) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 2:
                start_x, start_y = x, y
            elif grid[y][x] == 3:
                end_x, end_y = x, y

    def miro_bfs(start_x, start_y, end_x, end_y):
        stack = deque([(start_x, start_y, 0)])
        visited = [[0 for _ in range(N)] for _ in range(N)]
        visited[start_y][start_x] = 1
        while stack:
            cur_x, cur_y, cur_move = stack.popleft()
            for x, y in direction:
                new_x, new_y = cur_x + x, cur_y + y
                if 0 <= new_x < N and 0 <= new_y < N and (grid[new_y][new_x] == 0 or grid[new_y][new_x] == 3) and visited[new_y][new_x] == 0:
                    if new_x == end_x and new_y == end_y:
                        return cur_move
                    stack.append((new_x, new_y, cur_move + 1))
                    visited[new_y][new_x] = 1

    result = miro_bfs(start_x, start_y, end_x, end_y)
    if result == None:
        print(f'#{t} 0')
    else:
        print(f'#{t} {result}')