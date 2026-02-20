T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(input()) for _ in range(N)]

    flag = False
    for y in range(N):
        for x in range(N - M + 1):
            one_line = grid[y][x:x + M]
            start, end = 0, M - 1
            while (one_line[start] == one_line[end]) and start < end:
                start = start + 1
                end = end - 1
            if start >= end:
                print(f"#{t} {''.join(one_line)}")
                flag = True
    if not flag:
        grid = list(zip(*grid))
        for y in range(N):
            for x in range(N - M + 1):
                one_line = grid[y][x:x + M]
                start, end = 0, M - 1
                while (one_line[start] == one_line[end]) and start < end:
                    start = start + 1
                    end = end - 1
                if start >= end:
                    print(f'#{t} {"".join(one_line)}')