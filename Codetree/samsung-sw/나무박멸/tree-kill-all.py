from collections import defaultdict
N, M, K, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

tree_place = set()
total_delete = 0
delete_place = [[-1 for _ in range(N)] for _ in range(N)]
for y in range(N):
    for x in range(N):
        if grid[y][x] != 0 and grid[y][x] != -1:
            tree_place.add((x, y))

for year in range(M):
    for y in range(N):
        for x in range(N):
            if delete_place[y][x] != - 1 and delete_place[y][x] + C + 1 == year:
                delete_place[y][x] = -1
                grid[y][x] = 0
    
    new_grid = [list(grid[idx]) for idx in range(N)]
    new_tree_place = set(tree_place)
    for tree_x, tree_y in tree_place:
        cur_tree = 0
        not_tree = 0
        for add_x, add_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = tree_x + add_x, tree_y + add_y
            if 0 <= new_x < N and 0 <= new_y < N:
                if grid[new_y][new_x] >= 1:
                    cur_tree += 1
                elif grid[new_y][new_x] == 0:
                    not_tree += 1
        new_grid[tree_y][tree_x] += cur_tree
        for add_x, add_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = tree_x + add_x, tree_y + add_y
            if 0 <= new_x < N and 0 <= new_y < N and grid[new_y][new_x] == 0:
                new_grid[new_y][new_x] += new_grid[tree_y][tree_x] // not_tree
                if new_grid[new_y][new_x] != 0:
                    new_tree_place.add((new_x, new_y))
    
    if not new_tree_place:
        del_tree = 0
        del_x = 0
        del_y = 0
        break
    del_tree, del_x, del_y = 0, N - 1, N - 1
    for new_tree_x, new_tree_y in new_tree_place:
        cur_del = new_grid[new_tree_y][new_tree_x]
        for mul_x, mul_y in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for mul_num in range(1, K + 1):
                new_x, new_y = new_tree_x + (mul_x * mul_num), (new_tree_y + mul_y * mul_num)
                if 0 <= new_x < N and 0 <= new_y < N:
                    if new_grid[new_y][new_x] in (0, -1, -100):
                        break
                    elif new_grid[new_y][new_x] >= 1:
                        cur_del += new_grid[new_y][new_x]
        if cur_del > del_tree:
            del_tree = cur_del
            del_x, del_y = new_tree_x, new_tree_y
        elif cur_del == del_tree:
            if new_tree_y < del_y:
                del_x, del_y = new_tree_x, new_tree_y
            elif new_tree_y == del_y and new_tree_x < del_x:
                del_x, del_y = new_tree_x, new_tree_y
    
    total_delete += del_tree
    new_grid[del_y][del_x] = -100
    delete_place[del_y][del_x] = year
    for mul_x, mul_y in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for mul_num in range(1, K + 1):
                new_x, new_y = del_x + mul_x * mul_num, del_y + mul_y * mul_num
                if 0 <= new_x < N and 0 <= new_y < N:
                    if new_grid[new_y][new_x] in (0, -1):
                        if new_grid[new_y][new_x] == 0:
                            new_grid[new_y][new_x] = -100
                            delete_place[new_y][new_x] = year
                        break
                    elif new_grid[new_y][new_x] == -100:
                        new_grid[new_y][new_x] = -100
                        delete_place[new_y][new_x] = year
                        break
                    elif new_grid[new_y][new_x] >= 1:
                        new_grid[new_y][new_x] = -100
                        delete_place[new_y][new_x] = year

    grid = new_grid
    tree_place = set()
    for y in range(N):
        for x in range(N):
            if new_grid[y][x] >= 1:
                tree_place.add((x, y))

print(total_delete)