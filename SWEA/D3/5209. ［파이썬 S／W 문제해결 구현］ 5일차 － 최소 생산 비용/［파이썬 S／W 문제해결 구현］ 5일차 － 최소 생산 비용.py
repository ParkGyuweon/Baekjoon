T = int(input())

def factory(money, idx):
    global min_val
    if money >= min_val:
        return

    if sum(x_list) == N:
        min_val = min(min_val, money)

    for x in range(N):
        if not x_list[x]:
            x_list[x] = True
            factory(money + grid[idx][x], idx + 1)
            x_list[x] = False

for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    x_list = [False] * N
    min_val = 10E10

    factory(0, 0)
    print(f'#{t} {min_val}')