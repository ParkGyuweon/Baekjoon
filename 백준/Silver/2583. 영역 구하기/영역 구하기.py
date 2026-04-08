from collections import deque
M, N, K = map(int, input().split())
grid = [[0 for _ in range(N)] for _ in range(M)]
checked = [[0 for _ in range(N)] for _ in range(M)]
nemo_size, total_size = [], 0
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(K):
    DL_x, DL_y, UR_x, UR_y = map(int, input().split())
    for y in range(DL_y, UR_y):
        for x in range(DL_x, UR_x):
            grid[y][x] = 1

for y in range(M):
    for x in range(N):
        if grid[y][x] == 0 and checked[y][x] == 0:
            checked[y][x] = 1
            stack = deque([(x, y)])
            cur_size = 0
            while stack:
                cur_x, cur_y = stack.popleft()
                cur_size += 1
                for add_x, add_y in direction:
                    new_x, new_y = cur_x + add_x, cur_y + add_y
                    if 0 <= new_x < N and 0 <= new_y < M and grid[new_y][new_x] == 0 and checked[new_y][new_x] == 0:
                        checked[new_y][new_x] = 1
                        stack.append((new_x, new_y))
            nemo_size.append(cur_size)
            total_size += 1

print(total_size)
print(' '.join(map(str, list(sorted(nemo_size)))))