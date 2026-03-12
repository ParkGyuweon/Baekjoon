T = int(input())

for t in range(1, T + 1):
    N = int(input())
    block = [list(map(int, input().split())) for _ in range(N)]
    case_num = 0

    for first in range(N):
        for second in range(first, N):
            if (block[first][0] < block[second][0] and block[first][1] > block[second][1]) or (block[first][0] > block[second][0] and block[first][1] < block[second][1]):
                case_num += 1

    print(f'#{t} {case_num}')