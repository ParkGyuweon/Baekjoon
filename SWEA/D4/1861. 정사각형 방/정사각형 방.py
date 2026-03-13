T = int(input())
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def room_bfs(start_x, start_y):
    stack = [(start_x, start_y, 1)]
    while stack:
        cur_x, cur_y, cur_room = stack.pop(0)
        for x, y in direction:
            new_x, new_y = cur_x + x, cur_y + y
            if 0 <= new_x < N and 0 <= new_y < N and grid[new_y][new_x] - grid[cur_y][cur_x] == 1:
                if visited_room[new_y][new_x] != 0:
                    visited_room[start_y][start_x] = cur_room + visited_room[new_y][new_x]
                    return
                stack.append((new_x, new_y, cur_room + 1))
    visited_room[start_y][start_x] = cur_room

for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    visited_room = [[0 for _ in range(N)] for _ in range(N)]
    max_room = 0
    max_position = 0

    for y in range(N):
        for x in range(N):
            room_bfs(x, y)
            if visited_room[y][x] > max_room:
                max_room = visited_room[y][x]
                max_position = grid[y][x]
            elif visited_room[y][x] == max_room and max_position > grid[y][x]:
                max_position = grid[y][x]

    print(f'#{t} {max_position} {max_room}')