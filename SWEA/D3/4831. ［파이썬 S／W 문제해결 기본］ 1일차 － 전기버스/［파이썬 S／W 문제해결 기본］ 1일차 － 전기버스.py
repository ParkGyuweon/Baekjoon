T = int(input())

for t in range(T):
    K, N, M = map(int, input().split())
    stops = list(map(int, input().split()))

    current = 0
    position = 0
    destination = 0

    cur_flag = True
    for i in range(len(stops) - 1):
        if stops[i] + K < stops[i + 1]:
            cur_flag = False
    if not cur_flag:
        print(f'#{t + 1} 0')
    else:
        while position + K < N:
            for stop in stops:
                if position + K >= stop:
                    destination = stop
            position = destination
            current = current + 1
        print(f'#{t + 1} {current}')