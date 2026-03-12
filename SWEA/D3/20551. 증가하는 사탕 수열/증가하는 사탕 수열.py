T = int(input())
for t in range(1, T + 1):
    A, B, C = map(int, input().split())
    if C <= 2 or B <= 1:
        print(f'#{t} -1')
    else:
        operation = 0
        while B >= C:
            B -= 1
            operation += 1
        while A >= B:
            A -= 1
            operation += 1

        print(f'#{t} {operation}')