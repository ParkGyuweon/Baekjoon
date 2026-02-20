T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    hit_x, hit_y = list(range(M)), list(range(M))

    sum_list = []
    for i in range(M):
        for j in range(M):
            sum_list.append([hit_y[i], hit_x[j]])

    max_val = 0
    for row in range(N - M + 1):
        for col in range(N - M + 1):
            sum_val = 0
            for i in range(M * M):
                sum_val = sum_val + grid[row + sum_list[i][0]][col + sum_list[i][1]]
            if max_val < sum_val:
                max_val = sum_val
    print(f'#{t} {max_val}')