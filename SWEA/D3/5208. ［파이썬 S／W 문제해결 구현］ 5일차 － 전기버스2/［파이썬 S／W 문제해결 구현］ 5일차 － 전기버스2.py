T = int(input())


def bus(charge, start, end):
    global min_val

    if charge >= min_val:
        return

    if end >= N - 1:
        min_val = min(min_val, charge)
        return

    for item in range(start, end + 1):
        bus(charge + 1, item + 1, item + battery[item])


for t in range(1, T + 1):
    one_line = list(map(int, input().split()))
    N = one_line[0]
    battery = one_line[1:]
    min_val = 10E10
    bus(0, 1, battery[0])
    print(f'#{t} {min_val}')