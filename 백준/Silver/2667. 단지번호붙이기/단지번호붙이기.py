N = int(input())
grid = [list(map(int, list(input()))) for _ in range(N)]
danji_list = []
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cur_danji = 10
for y in range(N):
    for x in range(N):
        if grid[y][x] == 1:
            cur_num = 1
            stack = [(x, y)]
            grid[y][x] = cur_danji
            while stack:
                cur_x, cur_y = stack.pop(0)
                for add_x, add_y in direction:
                    new_x, new_y = cur_x + add_x, cur_y + add_y
                    if 0 <= new_x < N and 0 <= new_y < N and grid[new_y][new_x] == 1:
                        grid[new_y][new_x] = cur_danji
                        stack.append((new_x, new_y))
                        cur_num += 1
            cur_danji += 1
            danji_list.append(cur_num)
danji_list.sort()
print(len(danji_list))
for item in danji_list:
    print(item)