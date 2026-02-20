T = int(input())

for m in range(T):
    L = []
    N = int(input())
    for i in range(N):
    	L.append(list(map(int, input().split())))
    result = [0] * (N * N)
    for k in range(3):
        L_temp = []
        for i in range(N):
            sum = ''
            for j in range(N - 1, -1, -1):
                sum = sum + str(L[j][i])
            L_temp.append(list(sum))
            result[i * 3 + k] = sum
        L = L_temp

    print(f'#{m + 1}')
    for i in range(N):
        for j in range(3):
            print(''.join(result[i * 3 + j]), end = ' ')
        print('')