N = int(input())
L = [[0] * N for _ in range(N)]
def define(N, y, x):
    if N == 1:
        return '*'
    if y >= N // 3 and y < N // 3 * 2:
        if x >= N // 3 and x < N // 3 * 2:
            return ' '
    return define(N // 3, y % (N // 3), x % (N // 3))

for i in range(N):
    for j in range(N):
        if i < N // 3 and j < N // 3:
            L[i][j] = define(N, i, j)
        elif i >= N // 3 and i < N // 3 * 2:
            if j >= N // 3 and j < N // 3 * 2:
                L[i][j] = ' '
            else:
                L[i][j] = L[i % (N // 3)][j % (N // 3)]    
        else:
            L[i][j] = L[i % (N // 3)][j % (N // 3)]

for row in L:
    print(''.join(row))