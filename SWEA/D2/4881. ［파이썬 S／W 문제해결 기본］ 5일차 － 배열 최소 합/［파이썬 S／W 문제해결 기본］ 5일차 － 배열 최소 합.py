T = int(input())

def back(combination, N, y, x_list):
    global min_val
    if sum(combination) > min_val:
        return
    if len(combination) == N:
        if sum(combination) < min_val:
            min_val = sum(combination)
        return
    for j in range(N):
        if j in x_list:
            continue
        combination.append(grid[y][j])
        x_list.append(j)
        back(combination, N, y + 1, x_list)
        x_list.pop()
        combination.pop()

for t in range(1, T + 1):
    min_val = 10E10
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    back([], N, 0, [])
    print(f'#{t} {min_val}')
