T = int(input())

for t in range(1, T + 1):
    N = int(input())
    for num in range(1, int(N ** (1/3)) + 2):
        if num ** 3 == N:
            print(f'#{t} {num}')
            break
    else:
        print(f'#{t} -1')