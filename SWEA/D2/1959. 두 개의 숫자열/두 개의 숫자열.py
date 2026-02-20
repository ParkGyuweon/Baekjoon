T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    N_L = list(map(int, input().split()))
    M_L = list(map(int, input().split()))
    
    max = -1.0E10
    if N > M:
        for j in range(N - M + 1):
            sum = 0
            for k in range(M):
            	sum = sum + (N_L[j + k] * M_L[k])
            if sum > max :
            	max = sum
    elif M > N:
        for j in range(M - N + 1):
            sum = 0
            for k in range(N):
                sum = sum + (N_L[k] * M_L[j + k])
            if sum > max :
                max = sum
    else:
        for j in range(N):
            sum = sum + (N_L[j] * M_L[j])
        max = sum
    print(f'#{i + 1} {max}')