T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    min_v = arr[0]

    for num in arr:
        if num > max_v:
            max_v = num
        elif num < min_v:
            min_v = num

    print(f'#{tc} {max_v - min_v}')