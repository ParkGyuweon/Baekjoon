def dfs(start_x, start_y, end_x, end_y):
    stack = [(start_x, start_y, 0)]
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [(start_x, start_y)]

    while stack:
        cur_x, cur_y, time = stack.pop()
        for i in range(4):
            new_x, new_y = cur_x + direction[i][0], cur_y + direction[i][1]
            if (0 <= new_x < 16) and (0 <= new_y < 16) and (grid[new_y][new_x] == 0 or grid[new_y][new_x] == 3) and (new_x, new_y) not in visited:
                if grid[new_y][new_x] == 3:
                    return 1
                stack.append((new_x, new_y, time + 1))
                visited.append((new_x, new_y))

for t in range(1, 11):
    T = int(input())
    grid = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        if 2 in grid[i]:
            start_x, start_y = grid[i].index(2), i
        if 3 in grid[i]:
            end_x, end_y = grid[i].index(3), i

    result = dfs(start_x, start_y, end_x, end_y)
    if result == None:
        print(f'#{T} 0')
    else:
        print(f'#{T} 1')