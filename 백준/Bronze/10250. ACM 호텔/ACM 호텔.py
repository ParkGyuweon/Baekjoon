T = int(input())

for t in range(1, T + 1):
    H, W, N = map(int, input().split())
    if (N % H) == 0:
        Y = str(H)
    else:
        Y = str(N % H)
    if N // H == N / H:
        if len(str(N // H)) == 1:
            X = '0' + str(N // H)
        else:
            X = str(N // H)
    else:
        if len(str(N // H + 1)) == 1:
            X = '0' + str(N // H + 1)
        else:
            X = str(N // H + 1)
    print(Y + X)