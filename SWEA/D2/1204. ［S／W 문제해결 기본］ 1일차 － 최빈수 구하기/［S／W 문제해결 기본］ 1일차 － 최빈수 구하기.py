T = int(input())

for i in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    D = {}
    for j in range(len(L)):
        num = L[j]
        if num in D:
            D[num] = D[num] + 1
        else:
            D[num] = 1
    result = sorted(D.items(), key = lambda x : (-x[1], -x[0]))
    answer = result[0][0]
    print(f'#{N} {answer}')