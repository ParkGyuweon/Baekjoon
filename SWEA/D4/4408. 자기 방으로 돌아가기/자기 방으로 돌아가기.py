T = int(input())

for t in range(1,  T + 1):
    N = int(input())
    corridor_cnt = [0] * 200

    for i in range(N):
        start_room, end_room = map(int, input().split())
        min_room = min((start_room - 1) // 2, (end_room - 1) // 2)
        max_room = max((start_room - 1) // 2, (end_room - 1) // 2)
        for j in range(min_room, max_room + 1):
            corridor_cnt[j] += 1

    print(f'#{t} {max(corridor_cnt)}')