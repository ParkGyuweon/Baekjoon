N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = set()
cctv_list = []
min_val = 64

for y in range(N):
    for x in range(M):
        if grid[y][x] != 0:
            visited.add((x, y))
            if grid[y][x] != 6:
                cctv_list.append((x, y, grid[y][x]))

def camera(grid, cur_x, cur_y, direction):
    temp = set()
    if direction == 'L':
        new_x = cur_x - 1
        while new_x >= 0 and grid[cur_y][new_x] != 6:
            if grid[cur_y][new_x] == 0:
                temp.add((new_x, cur_y))
            new_x = new_x - 1
    elif direction == 'R':
        new_x = cur_x + 1
        while new_x < M and grid[cur_y][new_x] != 6:
            if grid[cur_y][new_x] == 0:
                temp.add((new_x, cur_y))
            new_x = new_x + 1
    elif direction == 'D':
        new_y = cur_y + 1
        while new_y < N and grid[new_y][cur_x] != 6:
            if grid[new_y][cur_x] == 0:
                temp.add((cur_x, new_y))
            new_y = new_y + 1
    elif direction == 'U':
        new_y = cur_y - 1
        while new_y >= 0 and grid[new_y][cur_x] != 6:
            if grid[new_y][cur_x] == 0:
                temp.add((cur_x, new_y))
            new_y = new_y - 1
    return temp

def case(CCTV):
    if CCTV == 1:
        return [('L'), ('R'), ('U'), ('D')]
    if CCTV == 2:
        return [('L', 'R'), ('U', 'D')]
    if CCTV == 3:
        return [('U', 'R'), ('R', 'D'), ('D', 'L'), ('L', 'U')]
    if CCTV == 4:
        return [('U', 'R', 'D'), ('L', 'R', 'D'), ('L', 'U', 'D'), ('L', 'U', 'R')]
    if CCTV == 5:
        return [('L', 'U', 'R', 'D')]

def back(visited, start, current):
    global min_val
    if len(current) == len(cctv_list):
        new_visited = set(visited)
        for x, y, direction in current:
            for dir in direction:
                new_visited = new_visited | camera(grid, x, y, dir)
        if (N * M) - len(new_visited) < min_val:
            min_val = (N * M) - len(new_visited)
        return

    for i in range(start, len(cctv_list)):
        for direction in case(cctv_list[i][2]):
            current.append((cctv_list[i][0], cctv_list[i][1], direction))
            back(visited, i + 1, current)
            current.pop()

back(visited, 0, [])
print(min_val)