from collections import deque
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
checked = [[0 for _ in range(M)] for _ in range(N)]
max_paint, total_paint = 0, 0
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for y in range(N):
    for x in range(M):
        if grid[y][x] == 1 and checked[y][x] == 0:
            checked[y][x] = 1
            stack = deque([(x, y)])
            cur_paint = 0
            while stack:
                cur_x, cur_y = stack.popleft()
                cur_paint += 1
                for add_x, add_y in direction:
                    new_x, new_y = cur_x + add_x, cur_y + add_y
                    if 0 <= new_x < M and 0 <= new_y < N and grid[new_y][new_x] == 1 and checked[new_y][new_x] == 0:
                        checked[new_y][new_x] = 1
                        stack.append((new_x, new_y))
            max_paint = max(max_paint, cur_paint)
            total_paint += 1

print(total_paint)
print(max_paint)