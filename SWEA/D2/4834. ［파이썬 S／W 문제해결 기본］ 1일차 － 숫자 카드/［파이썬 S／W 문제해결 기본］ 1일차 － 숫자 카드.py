T = int(input())
for t in range(T):
    N = int(input())
    ai = list(map(int, input()))

    max_val = 0
    num = 0
    for i in range(10):
        if ai.count(i) >= max_val:
            num = i
            max_val = ai.count(i)

    print(f'#{t + 1} {num} {max_val}')