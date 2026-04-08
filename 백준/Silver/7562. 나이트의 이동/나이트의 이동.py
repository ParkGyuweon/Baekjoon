from collections import deque
T = int(input())
direction = [(-1, -2), (-2, -1), (1, -2), (2, -1), (-1, 2), (-2, 1), (2, 1), (1, 2)]

def stack_bfs(start_x, start_y, end_x, end_y):
    stack = deque([(start_x, start_y, 0)])
    visited = [[0 for _ in range(I)] for _ in range(I)]
    visited[start_y][start_x] = 1

    while stack:
        cur_x, cur_y, cur_move = stack.popleft()
        for x, y in direction:
            new_x, new_y = cur_x + x, cur_y + y
            if 0 <= new_x < I and 0 <= new_y < I and visited[new_y][new_x] == 0:
                if new_x == end_x and new_y == end_y:
                    print(cur_move + 1)
                    return
                stack.append((new_x, new_y, cur_move + 1))
                visited[new_y][new_x] = 1

for t in range(1, T + 1):
    I = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    if start_x == end_x and start_y == end_y:
        print(0)
    else:
        stack_bfs(start_x, start_y, end_x, end_y)
