T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    catch_pari = [(i, j) for i in range(M) for j in range(M)]
    max_val = 0

    for y in range(N - M + 1):
        for x in range(N - M + 1):
            cur_sum = 0
            for add_x, add_y in catch_pari:
                cur_sum += grid[add_y + y][add_x + x]
            max_val = max(max_val, cur_sum)

    print(f'#{t} {max_val}')