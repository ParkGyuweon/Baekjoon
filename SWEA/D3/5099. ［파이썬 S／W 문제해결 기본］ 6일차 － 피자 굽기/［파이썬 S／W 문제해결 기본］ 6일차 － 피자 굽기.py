T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    pizza_list = list(map(int, input().split()))
    pizza = []

    for i in range(M):
        pizza.append([pizza_list[i], i + 1, 0])

    current = []

    for i in range(N):
        current.append(pizza.pop(0))

    while True:
        if not pizza and current.count(0) == N - 1:
            break
        if current[0] != 0 and current[0][0] == 0:
            current.pop(0)
            if pizza:
                current.insert(0, pizza.pop(0))
            else:
                current.insert(0, 0)
        current.append(current.pop(0))
        for item in current:
            if str(type(item)) == "<class 'list'>":
                item[2] = item[2] + 1
                if item[2] >= N:
                    item[0] = item[0] // 2
                    item[2] = 0
    for item in current:
        if item != 0:
            print(f'#{t} {item[1]}')