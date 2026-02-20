T = int(input())

def back(current_width):
    global cnt
    if (N - current_width) in memo:
        cnt = cnt + memo[N - current_width]
        return
    if current_width >= N:
        if current_width == N:
            cnt = cnt + 1
        return
    for item, width in nemo:
        back(current_width + width)

memo = {}
for t in range(1, T + 1):
    N = int(input())
    nemo = [('1', 10), ('22', 20), ('3', 20)]
    current_width, stack, cnt = 0, [], 0

    back(0)
    memo[N] = cnt
    print(f'#{t} {cnt}')