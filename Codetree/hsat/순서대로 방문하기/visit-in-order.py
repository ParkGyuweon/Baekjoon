from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
places = []

for _ in range(M):
    y, x = map(int, input().split())
    places.append((x - 1, y - 1))

visited = [[0 for _ in range(N)] for _ in range(N)]
visited[places[0][1]][places[0][0]] = 1
queue = deque([[places[0][0], places[0][1], visited]])

for place_idx in range(1, M):
    place = places[place_idx]
    next_queue = []
    while queue:
        cur_x, cur_y, cur_visited = queue.popleft()
        for add_x, add_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_visited = [list(cur_visited[i]) for i in range(N)]
            new_x, new_y = cur_x + add_x, cur_y + add_y
            if 0 <= new_x < N and 0 <= new_y < N and grid[new_y][new_x] == 0 and new_visited[new_y][new_x] == 0:
                if new_x == place[0] and new_y == place[1]:
                    new_visited[new_y][new_x] = 1
                    next_queue.append((new_x, new_y, new_visited))
                else:
                    new_visited[new_y][new_x] = 1
                    queue.append([new_x, new_y, new_visited])
    queue = deque(next_queue)

print(len(next_queue))