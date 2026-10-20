from collections import deque

def solution(maps):
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    answer = []
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] != 'X' and visited[y][x] == 0:
                stack = deque([(x, y)])
                cur_island = [int(maps[y][x])]
                visited[y][x] = 1
                while stack:
                    cur_x, cur_y = stack.popleft()
                    for add_x, add_y in direction:
                        new_x, new_y = cur_x + add_x, cur_y + add_y
                        if 0 <= new_x < len(maps[0]) and 0 <= new_y < len(maps) and maps[new_y][new_x] != 'X' and visited[new_y][new_x] == 0:
                            visited[new_y][new_x] = 1
                            stack.append((new_x, new_y))
                            cur_island.append(int(maps[new_y][new_x]))
                answer.append(sum(cur_island))
                
    if not answer:
        return [-1]
    return sorted(answer)