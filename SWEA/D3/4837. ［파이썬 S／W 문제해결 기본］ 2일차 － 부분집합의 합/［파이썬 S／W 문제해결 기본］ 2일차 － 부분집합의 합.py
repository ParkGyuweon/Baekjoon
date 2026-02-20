T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    cnt = 0
    
    for i in range(1 << 12):
        current = []
        for j in range(12):
            if i & (1 << j):
                current.append(number[j])
        if len(current) == N and sum(current) == K:
            cnt = cnt + 1
    print(f'#{t} {cnt}')