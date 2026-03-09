direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(grid, visited, item):
    global island_num
    stack = [item]
    visited.append(item)
    while stack:
        cur_x, cur_y = stack.pop(0)
        for x, y in direction:
            new_x, new_y = cur_x + x, cur_y + y
            if 0 <= new_x < M and 0 <= new_y < N and (new_x, new_y) in grid and (new_x, new_y) not in visited:
                stack.append((new_x, new_y))
                visited.append((new_x, new_y))
    island_num += 1


T = int(input())
for t in range(1, T + 1):
    M, N, K = map(int, input().split())
    grid = [tuple(map(int, input().split())) for _ in range(K)]
    island_num = 0
    visited = []
    for item in grid:
        if item not in visited:
            bfs(grid, visited, item)
    print(island_num)