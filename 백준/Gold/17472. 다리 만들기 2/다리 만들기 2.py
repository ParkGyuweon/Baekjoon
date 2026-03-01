from collections import defaultdict

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 한 개의 섬이 모든 섬에 도달 가능하면 다리 기준을 준수하는 것
# 가로 방향에 또 다른 섬이 있으면 연결 가능
# 세로 방향에 또 다른 섬이 있으면 연결 가능
# 하나의 다리를 추가할 때마다 기준을 준수하는 지 확인
# 기준을 준수하면 최소 여부를 판단
# 섬의 개수가 6개 뿐이니까... 가로 세로로 가능한 경우를 미리 만들어두고
# 거기서의 부분집합으로 각 경우를 판단해볼까?
# 섬 판단은 어떻게 해야 할까...

graph = {}
new_island = [defaultdict(list), defaultdict(list)]
island_num = 10
min_val = 10E10
for y in range(N): # 섬 찾기
    for x in range(M):
        if grid[y][x] == 1:
            candidate = [(x, y)]
            while candidate:
                cur_x, cur_y = candidate.pop(0)
                grid[cur_y][cur_x] = island_num
                new_island[0][cur_x].append(cur_y)
                new_island[1][cur_y].append(cur_x)
                if cur_y - 1 >= 0 and grid[cur_y - 1][cur_x] == 1 and (cur_x, cur_y - 1) not in candidate:
                    candidate.append((cur_x, cur_y - 1))
                if cur_y + 1 < N and grid[cur_y + 1][cur_x] == 1 and (cur_x, cur_y + 1) not in candidate:
                    candidate.append((cur_x, cur_y + 1))
                new_left, new_right = cur_x - 1, cur_x + 1
                while 0 <= new_left and grid[cur_y][new_left] == 1:
                    new_island[0][new_left].append(cur_y)
                    new_island[1][cur_y].append(new_left)
                    grid[cur_y][new_left] = island_num
                    if cur_y + 1 < N and grid[cur_y + 1][new_left] == 1 and (new_left, cur_y + 1) not in candidate:
                        candidate.append((new_left, cur_y + 1))
                    if cur_y - 1 >= 0 and grid[cur_y - 1][new_left] == 1 and (new_left, cur_y - 1) not in candidate:
                        candidate.append((new_left, cur_y - 1))
                    new_left -= 1
                while new_right < M and grid[cur_y][new_right] == 1:
                    new_island[0][new_right].append(cur_y)
                    new_island[1][cur_y].append(new_right)
                    grid[cur_y][new_right] = island_num
                    if cur_y + 1 < N and grid[cur_y + 1][new_right] == 1 and (new_right, cur_y + 1) not in candidate:
                        candidate.append((new_right, cur_y + 1))
                    if cur_y - 1 >= 0 and grid[cur_y - 1][new_right] == 1 and (new_right, cur_y - 1) not in candidate:
                        candidate.append((new_right, cur_y - 1))
                    new_right += 1

            graph[island_num] = new_island
            new_island = [defaultdict(list), defaultdict(list)]
            island_num += 1

last_island = 0
total = set()
connection = {}
for y in range(N): # 가로로 연결될 수 있는 섬 찾기
    last_island = 0
    last_x = 0
    for x in range(M):
        if grid[y][x] != 0:
            if last_island != grid[y][x] and last_island != 0:
                cur_val = x - last_x
                min_island = min(last_island, grid[y][x])
                max_island = max(last_island, grid[y][x])
                if cur_val >= 3:
                    total.add((min_island, max_island, 1))
                    if ((min_island, max_island, 1) in connection and connection[(min_island, max_island, 1)] > cur_val - 1) or (min_island, max_island, 1) not in connection:
                        connection[(min_island, max_island, 1)] = cur_val - 1
            last_island = grid[y][x]
            last_x = x

for x in range(M): # 세로로 연결될 수 있는 섬 찾기
    last_island = 0
    last_y = 0
    for y in range(N):
        if grid[y][x] != 0:
            if last_island != grid[y][x] and last_island != 0:
                cur_val = y - last_y
                min_island = min(last_island, grid[y][x])
                max_island = max(last_island, grid[y][x])
                if cur_val >= 3:
                    total.add((min_island, max_island, 2))
                    if ((min_island, max_island, 2) in connection and connection[
                        (min_island, max_island, 2)] > cur_val - 1) or (min_island, max_island, 2) not in connection:
                        connection[(min_island, max_island, 2)] = cur_val - 1
            last_island = grid[y][x]
            last_y = y

total = list(total)
partial = []

for i in range(1, 1 << len(total)): # 부분 집합 구하는 부분
    current = []
    for j in range(len(total)):
        if i & (1 << j):
            current.append(total[j])
    partial.append(current)

flag = False
for case in partial:
    current = defaultdict(list)
    stack = [10]
    visited = [10]
    for item in case:
        current[item[0]].append(item[1])
        current[item[1]].append(item[0])

    while stack:
        position = stack.pop(0)
        if position in current:
            for island in current[position]:
                if island not in visited:
                    stack.append(island)
                    visited.append(island)

    if len(visited) != island_num - 10:
        continue
    else:
        flag = True
        sum_val = 0
        for item in case:
            sum_val += connection[item]
        if min_val > sum_val:
            min_val = sum_val
if not flag:
    print(-1)
else:
    print(min_val)