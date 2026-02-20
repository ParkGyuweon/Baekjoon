T = int(input())

for tc in range(1, T + 1):
    max_val = 0
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        low = 0
        for j in range(i + 1, N):
            if arr[i] > arr[j]:
                low = low + 1
        if low > max_val:
        	max_val = low

    print(f'#{tc} {max_val}')