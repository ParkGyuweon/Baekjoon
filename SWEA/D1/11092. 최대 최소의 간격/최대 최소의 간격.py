T = int(input())
for t in range(1, T + 1):
    N = int(input())
    number = list(map(int, input().split()))
    min_idx, max_idx = 0, 0
    
    for i in range(1, N):
        if number[i] < number[min_idx]:
            min_idx = i
        if number[i] >= number[max_idx]:
            max_idx = i
            
    print(f'#{t} {abs(max_idx - min_idx)}')