N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for y in range(N):
    for x in range(M):
        if grid[y][x] == 'I':
            start_x, start_y = x, y
            break

stack = [(start_x, start_y)]
people_num = 0
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[start_y][start_x] = 1
while stack:
    cur_x, cur_y = stack.pop(0)
    for x, y in direction:
        new_x, new_y = cur_x + x, cur_y + y
        if 0 <= new_x < M and 0 <= new_y < N and grid[new_y][new_x] != 'X' and visited[new_y][new_x] == 0:
            if grid[new_y][new_x] == 'P':
                people_num += 1
            stack.append((new_x, new_y))
            visited[new_y][new_x] = 1
if people_num == 0:
    print('TT')
else:
    print(people_num)