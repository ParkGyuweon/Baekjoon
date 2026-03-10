T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    partial_num = 0
    
    for i in range(1 << 12):
        current = []
        for j in range(12):
            if i & (1 << j):
                current.append(j + 1)
        if len(current) == N and sum(current) == K:
            partial_num += 1
    
    print(f'#{t} {partial_num}')