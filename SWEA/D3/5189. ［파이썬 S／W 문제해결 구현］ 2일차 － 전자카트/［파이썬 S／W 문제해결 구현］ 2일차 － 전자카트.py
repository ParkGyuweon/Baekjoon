T = int(input())

def dfs(grid):
    global min_val
    stack = [(0, 0, [0])]
    while stack:
        cur_position, cur_sum, cur_visited = stack.pop()
        for i in range(N):
            if i not in cur_visited:
                new_list = cur_visited[:]
                new_list.append(i)
                if len(new_list) == N:
                    min_val = min(min_val, cur_sum + grid[cur_position][i] + grid[i][0])
                    break
                stack.append((i, cur_sum + grid[cur_position][i], new_list))

for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    min_val = 10E10
    dfs(grid)
    print(f'#{t} {min_val}')