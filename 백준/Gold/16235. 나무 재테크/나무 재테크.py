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

for year in range(K):
    # 봄
    dead_tree = []
    for y in range(N):
        for x in range(N):
            new_list = deque()
            for item in tree_grid[y][x]:
                if grid[y][x] >= item:
                    grid[y][x] -= item
                    new_list.append(item + 1)
                else:
                    dead_tree.append((y, x, item))
            tree_grid[y][x] = new_list

    # 여름
    for item in dead_tree:
        grid[item[0]][item[1]] += item[2] // 2
    dead_tree = []

    # 가을
    for y in range(N):
        for x in range(N):
            for item in tree_grid[y][x]:
                if item % 5 == 0:
                    for add_x, add_y in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                        new_x, new_y = x + add_x, y + add_y
                        if 0 <= new_x < N and 0 <= new_y < N:
                            tree_grid[new_y][new_x].appendleft(1)

    # 겨울
    for y in range(N):
        for x in range(N):
            grid[y][x] += add_nut[y][x]

sum_val = 0
for y in range(N):
    for x in range(N):
        sum_val += len(tree_grid[y][x])

print(sum_val)