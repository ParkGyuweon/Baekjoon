T = int(input())
for t in range(1, T + 1):
    N = int(input())
    number = list(map(int, input().split()))

    # 선택
    for i in range(0, N - 1):
        min_idx = i
        for j in range(i + 1, N):
            if number[j] < number[min_idx]:
                min_idx = j
        number[i], number[min_idx] = number[min_idx], number[i]
    print(f'#{t} {" ".join(map(str, number))}')