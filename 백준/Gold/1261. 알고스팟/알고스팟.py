from heapq import heappop, heappush
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
M, N = map(int, input().split())
queue = [(0, 0, 0)]
distance = [[float('INF') for _ in range(M)] for _ in range(N)]
distance[0][0] = 0
grid = [list(map(int, list(input()))) for _ in range(N)]

while queue:
    cur_weight, cur_x, cur_y = heappop(queue)
    if distance[cur_y][cur_x] < cur_weight:
        continue

    for x, y in direction:
        new_x, new_y = cur_x + x, cur_y + y
        if 0 <= new_x < M and 0 <= new_y < N:
            if grid[new_y][new_x] == 1:
                weight = 1
            else:
                weight = 0
            if distance[new_y][new_x] <= cur_weight + weight:
                continue
        else:
            continue
        distance[new_y][new_x] = cur_weight + weight
        heappush(queue, (cur_weight + weight, new_x, new_y))
print(distance[N - 1][M - 1])