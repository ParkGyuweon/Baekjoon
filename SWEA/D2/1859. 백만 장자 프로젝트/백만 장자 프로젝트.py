T = int(input())
for t in range(1, T + 1):
    N = int(input())
    value = list(map(int, input().split()))

    make_money = 0
    max_val = max(value)
    end_idx = value.index(max_val)

    while True:
        make_money += max_val * len(value[:end_idx]) - sum(value[:end_idx])
        value = value[end_idx + 1:]
        if not value:
            break
        max_val = max(value)
        end_idx = value.index(max_val)

    print(f'#{t} {make_money}')