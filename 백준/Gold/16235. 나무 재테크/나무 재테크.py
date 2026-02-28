import sys
input = sys.stdin.readline
from collections import deque

N, M, K = map(int, input().split())
add_nut = [list(map(int, input().split())) for _ in range(N)]
tree_grid = [[deque() for _ in range(N)] for _ in range(N)]
for idx in range(M):
    one_line = list(map(int, input().split()))
    tree_grid[one_line[0] - 1][one_line[1] - 1].append(one_line[2])
grid = [[5 for _ in range(N)] for _ in range(N)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
for year in range(K):
    # 봄
    for y in range(N):
        for x in range(N):
            add_sum = 0
            flag = True
            if not tree_grid[y][x]:
                continue
            for _ in range(len(tree_grid[y][x])):

                item = tree_grid[y][x].popleft()
                if flag and grid[y][x] >= item:
                    grid[y][x] -= item
                    tree_grid[y][x].append(item + 1)
                else:
                    flag = False
                    grid[y][x] += item // 2
                    continue

    # 가을
    for y in range(N):
        for x in range(N):
            grid[y][x] += add_nut[y][x]
            for item in tree_grid[y][x]:
                if item % 5 == 0:
                    for add_x, add_y in direction:
                        new_x, new_y = x + add_x, y + add_y
                        if 0 <= new_x < N and 0 <= new_y < N:
                            tree_grid[new_y][new_x].appendleft(1)

sum_val = 0
for y in range(N):
    for x in range(N):
        sum_val += len(tree_grid[y][x])

print(sum_val)



