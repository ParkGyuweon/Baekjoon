T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_v = -10E10
    min_v = 10e10
    
    for i in range(N - M + 1):
        sum_val = 0
        for j in range(M):
            sum_val = sum_val + arr[i + j]
        if sum_val > max_v:
            max_v = sum_val
        if sum_val < min_v:
            min_v = sum_val
            
    print(f'#{tc} {max_v - min_v}')