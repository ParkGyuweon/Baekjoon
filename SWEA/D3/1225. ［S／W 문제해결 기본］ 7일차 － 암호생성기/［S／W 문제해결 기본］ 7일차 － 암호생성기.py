for t in range(1, 11):
    T = int(input())
    data = list(map(int, input().split()))
    minus = 1
    while True:
        data.append(data.pop(0) - minus)
        minus += 1
        if data[-1] <= 0:
            data[-1] = 0
            break
        if minus == 6:
            minus = 1
    print(f'#{T} {" ".join(map(str, data))}')