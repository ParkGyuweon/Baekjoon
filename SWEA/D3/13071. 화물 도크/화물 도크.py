T = int(input())

def check(current):
    global max_car
    max_car = max(max_car, len(current))
    if len(current) == N:
        return
    for item in time_table:
        if ((not current) or (current and item not in current and current[-1][1] <= item[0])) and (item, len(current)) not in already_checked:
            already_checked.append((item, len(current)))
            current.append(item)
            check(current)
            current.pop()

for t in range(1, T + 1):
    N = int(input())
    time_table = [tuple(map(int, input().split())) for _ in range(N)]
    already_checked = []
    max_car = 0
    check([])
    print(f'#{t} {max_car}')