N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
fish_num = 0
check = [0] * 6
last_eat = 0
for y in range(N): # 아기 상어 위치 찾기
    for x in range(N):
        if grid[y][x] == 9:
            grid[y][x] = 0
            shark_x, shark_y, shark_size = x, y, 2
        elif grid[y][x] != 0:
            fish_num += 1
            check[grid[y][x] - 1] += 1
direction = [(0, -1), (-1, 0), (1, 0), (0, 1)] # 아기 상어 이동 위치
cur_time = 0
stack = [(shark_x, shark_y, 0, 0)]

def shark(grid, stack, shark_size, fish_num):
    global last_eat
    visited = []
    fish_list = []
    while stack:
        cur_x, cur_y, cur_time, eat_fish = stack.pop(0)
        for x, y in direction:
            new_x, new_y = cur_x + x, cur_y + y
            if 0 <= new_x < N and 0 <= new_y < N and grid[new_y][new_x] <= shark_size and (new_x, new_y) not in visited:
                if grid[new_y][new_x] < shark_size and grid[new_y][new_x] != 0:
                    if not fish_list:
                        min_dist = cur_time + 1
                    if fish_list and (cur_time + 1 != min_dist):
                        fish_list.sort(key=lambda x: (x[1], x[0]))
                        fish_x, fish_y, fish_time, fish_eat = fish_list.pop(0)
                        last_eat = fish_time
                        if fish_eat + 1 == shark_size:
                            shark_size += 1
                            stack = [(fish_x, fish_y, fish_time, 0)]
                        else:
                            stack = [(fish_x, fish_y, fish_time, fish_eat + 1)]
                        visited = []
                        fish_list = []
                        check[grid[fish_y][fish_x] - 1] -= 1
                        grid[fish_y][fish_x] = 0
                        fish_num -= 1
                        if fish_num == 0 or sum(check[:shark_size - 1]) == 0:
                            return min_dist
                        break
                    else:
                        if (new_x, new_y, cur_time + 1, eat_fish) not in fish_list:
                            fish_list.append((new_x, new_y, cur_time + 1, eat_fish))
                        if (new_x, new_y, cur_time + 1, eat_fish) not in stack:
                            stack.append((new_x, new_y, cur_time + 1, eat_fish))
                else:
                    stack.append((new_x, new_y, cur_time + 1, eat_fish))
                    visited.append((new_x, new_y))
        if fish_list and not stack:
            fish_list.sort(key=lambda x: (x[1], x[0]))
            fish_x, fish_y, fish_time, fish_eat = fish_list.pop(0)
            last_eat = fish_time
            if eat_fish + 1 == shark_size:
                shark_size += 1
                stack = [(fish_x, fish_y, fish_time, 0)]
            else:
                stack = [(fish_x, fish_y, fish_time, fish_eat + 1)]
            visited = []
            fish_list = []
            check[grid[fish_y][fish_x] - 1] -= 1
            grid[fish_y][fish_x] = 0
            fish_num -= 1
            if fish_num == 0 or sum(check[:shark_size - 1]) == 0:
                return fish_time
    return last_eat

print(shark(grid, stack, shark_size, fish_num))