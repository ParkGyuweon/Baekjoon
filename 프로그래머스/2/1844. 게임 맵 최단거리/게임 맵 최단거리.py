from collections import deque
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def solution(maps):
    queue = deque([(0, 0)])
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[0][0] = 1
    while queue:
        cur_x, cur_y = queue.popleft()
        for x, y in direction:
            new_x, new_y = cur_x + x, cur_y + y
            if 0 <= new_x < len(maps[0]) and 0 <= new_y < len(maps) and maps[new_y][new_x] == 1 and visited[new_y][new_x] == 0:
                if new_x == len(maps[0]) - 1 and new_y == len(maps) - 1:
                    return visited[cur_y][cur_x] + 1
                visited[new_y][new_x] = visited[cur_y][cur_x] + 1
                queue.append((new_x, new_y))
    return - 1