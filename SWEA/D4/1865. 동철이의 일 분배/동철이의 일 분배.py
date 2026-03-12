from decimal import *
getcontext().rounding = ROUND_HALF_UP
T = int(input())
 
def work(current_mul, grid, y):
    global max_possibility
    if current_mul <= max_possibility:
        return
     
    if sum(x_list) == N:
        max_possibility = max(max_possibility, current_mul)
        return
     
    for x in range(N):
        if not x_list[x]:
            x_list[x] = True
            work(current_mul * (grid[y][x] / 100), grid, y + 1)
            x_list[x] = False
                 
for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    x_list = [False] * N
    max_possibility = 0
    work(100, grid, 0)
    print(f'#{t} {Decimal(max_possibility).quantize(Decimal("0.000001"))}')