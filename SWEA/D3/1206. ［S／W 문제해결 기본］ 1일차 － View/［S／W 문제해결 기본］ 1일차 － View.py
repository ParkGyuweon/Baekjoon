for i in range(10):
    N = int(input())
    L = list(map(int, input().split()))
    sum = 0
    for j in range(2, N - 2):
        if L[j - 1] > L[j] or L[j - 2] > L[j]:
            continue
        if L[j + 1] > L[j] or L[j + 2] > L[j]:
            continue
        min_value = L[j] - max(L[j - 1], L[j - 2], L[j + 1], L[j + 2])
        sum = sum + min_value
    print(f'#{i + 1} {sum}')