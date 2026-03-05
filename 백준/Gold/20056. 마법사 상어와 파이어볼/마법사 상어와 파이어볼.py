from collections import defaultdict

N, M, K = map(int, input().split())
fireball = [list(map(int, input().split())) for _ in range(M)]
fireballs = defaultdict(list)

for item in fireball:
    fireballs[(item[1] - 1, item[0] - 1)].append((item[2], item[3], item[4]))

direction = {0 : (0, -1), 1: (1, -1), 2 : (1, 0), 3 : (1, 1), 4 : (0, 1), 5 : (-1, 1), 6 : (-1, 0), 7 : (-1, -1)}

for turn in range(K):
    current = defaultdict(list)
    for key, value in fireballs.items():
        for fire in value:
            new_x, new_y = (key[0] + (direction[fire[2]][0] * fire[1])) % N, (key[1] + (direction[fire[2]][1] * fire[1])) % N
            current[(new_x, new_y)].append(fire)
    for key, value in current.items():
        sum_weight, sum_speed, sum_direction, direction_flag = 0, 0, value[0][2] % 2, True
        if len(value) >= 2:
            item_number = len(value)
            for item in value:
                sum_weight += item[0]
                sum_speed += item[1]
                if item[2] % 2 != sum_direction:
                    direction_flag = False
            if sum_weight // 5 == 0:
                current[key] = []
                continue
            current[key] = []
            if direction_flag:
                for i in range(4):
                    current[key].append(((sum_weight // 5), (sum_speed // item_number), i * 2))
            else:
                for i in range(4):
                    current[key].append(((sum_weight // 5), (sum_speed // item_number), i * 2 + 1))
    fireballs = current

total_sum = 0

for key, value in fireballs.items():
    for item in value:
        total_sum += item[0]

print(total_sum)