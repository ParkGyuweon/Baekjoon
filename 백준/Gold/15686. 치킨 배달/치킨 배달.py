N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
chicken_shop = []
partial_chicken = []
homes = []
min_distance = 10E10

for y in range(N):
    for x in range(N):
        if grid[y][x] == 2:
            chicken_shop.append((x, y))
        elif grid[y][x] == 1:
            homes.append((x, y))

for i in range(1, 1 << len(chicken_shop)):
    current = []
    for j in range(len(chicken_shop)):
        if i & (1 << j):
            current.append(chicken_shop[j])
    if len(current) <= M:
        partial_chicken.append(current)

for chickens in partial_chicken:
    total_distance = 0
    for home in homes:
        home_distance = 10E10
        for chicken in chickens:
            if abs(chicken[0] - home[0]) + abs(chicken[1] - home[1]) < home_distance:
                home_distance = abs(chicken[0] - home[0]) + abs(chicken[1] - home[1])
        total_distance += home_distance
    if total_distance < min_distance:
        min_distance = total_distance

print(min_distance)