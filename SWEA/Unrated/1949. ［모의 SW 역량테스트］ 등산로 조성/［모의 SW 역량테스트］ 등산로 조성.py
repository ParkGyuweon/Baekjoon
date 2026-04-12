from collections import deque
T = int(input())
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def mountain_bfs(start_x, start_y):
    queue = deque([(start_x, start_y, False, (0, 0, 0), {(start_x, start_y)})])
    max_road = 0

    while queue:
        cur_x, cur_y, cur_flag, cur_cut, cur_set = queue.popleft()
        max_road = max(max_road, len(cur_set))

        for x, y in direction:
            new_x, new_y = cur_x + x, cur_y + y
            if 0 <= new_x < N and 0 <= new_y < N:
                if not cur_flag and (new_x, new_y) not in cur_set and grid[new_y][new_x] < grid[cur_y][cur_x]:
                    new_set = set(cur_set)
                    new_set.add((new_x, new_y))
                    queue.append((new_x, new_y, cur_flag, cur_cut, new_set))
                elif not cur_flag and (new_x, new_y) not in cur_set and grid[new_y][new_x] >= grid[cur_y][cur_x] and grid[new_y][new_x] - K < grid[cur_y][cur_x]:
                    new_set = set(cur_set)
                    new_set.add((new_x, new_y))
                    queue.append((new_x, new_y, True, (new_x, new_y, grid[cur_y][cur_x] - 1), new_set))
                elif cur_flag and (new_x, new_y) not in cur_set and not (cur_x == cur_cut[0] and cur_y == cur_cut[1]) and grid[new_y][new_x] < grid[cur_y][cur_x]:
                    new_set = set(cur_set)
                    new_set.add((new_x, new_y))
                    queue.append((new_x, new_y, cur_flag, cur_cut, new_set))
                elif cur_flag and (new_x, new_y) not in cur_set and cur_x == cur_cut[0] and cur_y == cur_cut[1] and grid[new_y][new_x] < cur_cut[2]:
                    new_set = set(cur_set)
                    new_set.add((new_x, new_y))
                    queue.append((new_x, new_y, cur_flag, cur_cut, new_set))

    return max_road

for t in range(1, T + 1):
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    max_list, max_value = [], 0
    global_max_road = 0

    for y in range(N):
        for x in range(N):
            if grid[y][x] > max_value:
                max_list = [(x, y)]
                max_value = grid[y][x]
            elif grid[y][x] == max_value:
                max_list.append((x, y))

    for item in max_list:
        global_max_road = max(global_max_road, mountain_bfs(item[0], item[1]))

    print(f'#{t} {global_max_road}')