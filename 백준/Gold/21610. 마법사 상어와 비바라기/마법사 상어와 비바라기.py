N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
cloud = [(0, N - 1), (1, N - 1), (0, N - 2), (1, N - 2)]
commands = [list(map(int, input().split())) for _ in range(M)] # 방향 거리
direction = {1 : (-1, 0), 2: (-1, -1), 3 : (0, -1), 4 : (1, -1), 5 : (1, 0), 6 : (1, 1), 7 : (0, 1), 8 : (-1, 1)}
cross = [(-1, 1), (-1, -1), (1, 1), (1, -1)]

for command in commands:
    water_up = set()
    for item in cloud:
        new_x, new_y = (item[0] + (direction[command[0]][0] * command[1])) % N, (item[1] + (direction[command[0]][1] * command[1])) % N
        grid[new_y][new_x] += 1
        water_up.add((new_x, new_y))
    for item in water_up:
        water_sum = 0
        for x, y in cross:
            new_x, new_y = item[0] + x, item[1] + y
            if 0 <= new_x < N and 0 <= new_y < N and grid[new_y][new_x] != 0:
                water_sum += 1
        grid[item[1]][item[0]] += water_sum
    new_cloud = []

    for y in range(N):
        for x in range(N):
            if grid[y][x] >= 2 and (x, y) not in water_up:
                new_cloud.append((x, y))
                grid[y][x] -= 2
    cloud = new_cloud

total_water = 0
for y in range(N):
    for x in range(N):
        total_water += grid[y][x]
print(total_water)