N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
start_x, start_y = N // 2, N // 2
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cur_x, cur_y, turn, cur_dir, move_one, move_two = start_x, start_y, 1, 0, 0, 0
wind = {0 : [(0, -2, 0.02), (-1, -1, 0.1), (0, -1, 0.07), (1, -1, 0.01), (-2, 0, 0.05), (-1, 1, 0.1), (0, 1, 0.07), (1, 1, 0.01), (0, 2, 0.02), (-1, 0, 10)],
        1 : [(-2, 0, 0.02), (1, 1, 0.1), (-1, 0, 0.07), (-1, -1, 0.01), (0, 2, 0.05), (-1, 1, 0.1), (1, 0, 0.07), (1, -1, 0.01), (2, 0, 0.02), (0, 1, 10)],
        2 : [(0, 2, 0.02), (1, -1, 0.1), (0, -1, 0.07), (-1, 1, 0.01), (2, 0, 0.05), (1, 1, 0.1), (0, 1, 0.07), (-1, -1, 0.01), (0, -2, 0.02), (1, 0, 10)],
        3 : [(-2, 0, 0.02), (1, -1, 0.1), (-1, 0, 0.07), (1, 1, 0.01), (0, -2, 0.05), (-1, -1, 0.1), (1, 0, 0.07), (-1, 1, 0.01), (2, 0, 0.02), (0, -1, 10)]}
total_morae = 0

def morae(grid, cur_x, cur_y, cur_dir):
    global total_morae
    cur_sum = 0
    for x, y, num in wind[cur_dir]:
        new_x, new_y = cur_x + x, cur_y + y
        if num != 10:
            if not (0 <= new_x < N and 0 <= new_y < N):
                total_morae += int((grid[cur_y][cur_x] * num))
                cur_sum += int(grid[cur_y][cur_x] * num)
            else:
                grid[new_y][new_x] += int(grid[cur_y][cur_x] * num)
                cur_sum += int(grid[cur_y][cur_x] * num)
        else:
            if not (0 <= new_x < N and 0 <= new_y < N):
                total_morae += int(grid[cur_y][cur_x] - cur_sum)
            else:
                grid[new_y][new_x] += int(grid[cur_y][cur_x] - cur_sum)

def tonaido(grid, cur_x, cur_y, turn, cur_dir, move_one, move_two):
    while True:
        while move_one < turn:
            new_x, new_y = cur_x + direction[cur_dir % 4][0], cur_y + direction[cur_dir % 4][1]
            morae(grid, new_x, new_y, cur_dir % 4)
            if new_x == 0 and new_y == 0:
                return
            grid[new_y][new_x] = 0
            cur_x, cur_y = new_x, new_y
            move_one += 1
        move_one = 0
        cur_dir += 1
        while move_two < turn:
            new_x, new_y = cur_x + direction[cur_dir % 4][0], cur_y + direction[cur_dir % 4][1]
            morae(grid, new_x, new_y, cur_dir % 4)
            if new_x == 0 and new_y == 0:
                return
            grid[new_y][new_x] = 0
            cur_x, cur_y = new_x, new_y
            move_two += 1
        move_two = 0
        cur_dir += 1
        turn += 1

tonaido(grid, cur_x, cur_y, turn, cur_dir, move_one, move_two)
print(total_morae)