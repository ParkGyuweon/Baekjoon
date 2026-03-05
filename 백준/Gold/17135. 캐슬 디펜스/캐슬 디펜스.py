N, M, D = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
partial_archer = []
initial_enemies = []
attack_sum = 0

for y in range(N):
    for x in range(M):
        if grid[y][x] == 1:
            initial_enemies.append((x, y))

for i in range(1 << M):
    current = []
    for j in range(M):
        if i & (1 << j):
            current.append((j, N))
    if len(current) == 3:
        partial_archer.append(list(current))

for archers in partial_archer:
    enemies = list(initial_enemies)
    cur_attack_sum = 0
    while enemies:
        attack_enemy = set()
        for archer in archers:
            min_dist = 10E10
            min_enemy = 0
            for enemy in enemies:
                cur_dist = abs(enemy[0] - archer[0]) + abs(enemy[1] - archer[1])
                if cur_dist <= D and cur_dist <= min_dist:
                    if cur_dist == min_dist and min_enemy[0] > enemy[0]:
                        min_enemy = enemy
                    elif cur_dist < min_dist:
                        min_dist = cur_dist
                        min_enemy = enemy
            if min_enemy != 0:
                attack_enemy.add(min_enemy)
        cur_attack_sum += len(attack_enemy)
        new_enemy = []
        for enemy in enemies:
            if enemy in attack_enemy:
                continue
            else:
                new_x, new_y = enemy[0], enemy[1] + 1
                if new_y >= N:
                    continue
                else:
                    new_enemy.append((new_x, new_y))
        enemies = new_enemy
    attack_sum = max(attack_sum, cur_attack_sum)
print(attack_sum)