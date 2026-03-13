T = int(input())
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def number_bfs(total_set):
    stack = [(i, j, grid[j][i]) for i in range(4) for j in range(4)]
    while stack:
        cur_x, cur_y, cur_str = stack.pop(0)
        for x, y in direction:
            new_x, new_y = cur_x + x, cur_y + y
            if 0 <= new_x < 4 and 0 <= new_y < 4:
                if len(cur_str + grid[new_y][new_x]) == 7:
                    total_set.add(cur_str + grid[new_y][new_x])
                else:
                    stack.append((new_x, new_y, cur_str + grid[new_y][new_x]))

for t in range(1, T + 1):
    total_set = set()
    grid = [list(input().split()) for _ in range(4)]
    number_bfs(total_set)
    print(f'#{t} {len(total_set)}')