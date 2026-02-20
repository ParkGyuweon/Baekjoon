T = int(input())

for t in range(1, T + 1):
    N, K = map(int, input().split())
    grid = [''.join(input().split()) for _ in range(N)]
    result = 0

    for i in range(N):
        one_line = grid[i].replace('01', '0-1')
        one_line = one_line.replace('10', '1-0')
        one_line = one_line.split('-')
        for item in one_line:
            if item == '1' * K:
                result = result + 1

    transpose_grid = list(zip(*grid))
    for i in range(N):
        one_line = ''.join(transpose_grid[i]).replace('01', '0-1')
        one_line = one_line.replace('10', '1-0')
        one_line = one_line.split('-')
        for item in one_line:
            if item == '1' * K:
                result = result + 1

    print(f'#{t} {result}')