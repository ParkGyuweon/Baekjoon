direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(10):
    t = int(input())
    grid = [list(map(int, list(input()))) for _ in range(16)]
    visited = [[0 for _ in range(16)] for _ in range(16)]
    
    for y in range(16):
        for x in range(16):
            if grid[y][x] == 2:
                start_x, start_y = x, y
            elif grid[y][x] == 3:
                end_x, end_y = x, y
    
    def miro_dfs(start_x, start_y, end_x, end_y):
        stack = [(start_x, start_y)]
        visited[start_y][start_x] = 1
        
        while stack:
            cur_x, cur_y = stack.pop()
            for x, y in direction:
                new_x, new_y = cur_x + x, cur_y + y
                if 0 <= new_x < 16 and 0 <= new_y < 16 and grid[new_y][new_x] in (0, 3) and visited[new_y][new_x] == 0:
                    if new_x == end_x and new_y == end_y:
                        return 1
                    stack.append((new_x, new_y))
                    visited[new_y][new_x] = 1
                    
        return 0
    
    print(f'#{t} {miro_dfs(start_x, start_y, end_x, end_y)}')
                        