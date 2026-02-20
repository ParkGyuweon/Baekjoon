T = int(input())
for t in range(1, T + 1):
    N = int(input())
    number = list(map(int, input().split()))
    
    for i in range(N - 1):
        if i % 2 == 0:
            max_idx = i
            for j in range(i + 1, N):
                if number[max_idx] < number[j]:
                    max_idx = j
            number[max_idx], number[i] = number[i], number[max_idx]
        else:
            min_idx = i
            for j in range(i + 1, N):
                if number[min_idx] > number[j]:
                    min_idx = j
            number[min_idx], number[i] = number[i], number[min_idx]
            
    print(f'#{t} {" ".join(map(str, number[0:10]))}')