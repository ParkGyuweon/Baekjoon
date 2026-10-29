from collections import deque

def solution(land):
    visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    cur_oil = 1
    oil_dir = {}
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for y in range(len(land)):
        for x in range(len(land[0])):
            if visited[y][x] == 0 and land[y][x] == 1:
                stack = deque([(x, y)])
                visited[y][x] = cur_oil
                oil_dir[cur_oil] = 1
                while stack:
                    cur_x, cur_y = stack.popleft()
                    for add_x, add_y in direction:
                        new_x, new_y = cur_x + add_x, cur_y + add_y
                        if 0 <= new_x < len(land[0]) and 0 <= new_y < len(land) and visited[new_y][new_x] == 0 and land[new_y][new_x] == 1:
                            visited[new_y][new_x] = cur_oil
                            stack.append((new_x, new_y))
                            oil_dir[cur_oil] += 1
                cur_oil += 1
    answer = 0
    for x in range(len(land[0])):
        row_visited = set()
        cur_sum = 0
        for y in range(len(land)):
            if visited[y][x] != 0 and visited[y][x] not in row_visited:
                cur_sum += oil_dir[visited[y][x]]
                row_visited.add(visited[y][x])
        answer = max(answer, cur_sum)
    return answer