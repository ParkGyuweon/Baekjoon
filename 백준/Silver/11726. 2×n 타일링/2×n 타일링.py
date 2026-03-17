N = int(input())
if N == 1:
    print(1)
else:
    memo = [0] * N
    memo[0], memo[1] = 1, 2
    
    for num in range(2, N):
        memo[num] = memo[num - 1] + memo[num - 2]
    
    print(memo[N - 1] % 10007)