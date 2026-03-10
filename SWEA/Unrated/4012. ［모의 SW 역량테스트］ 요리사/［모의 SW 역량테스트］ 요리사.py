T = int(input())

def back(current, start):
    global min_val
    if len(current) == N // 2:
        another = total - set(current)
        current_sum, another_sum = 0, 0
        for first in current:
            for second in current:
                current_sum += grid[first][second]

        for first in another:
            for second in another:
                another_sum += grid[first][second]
        min_val = min(min_val, abs(current_sum - another_sum))
        return

    for idx in range(start, N):
        current.append(idx)
        back(current, idx + 1)
        current.pop()

for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    total = set(list(range(N)))
    min_val = 10E10
    back([0], 1)
    print(f'#{t} {min_val}')