from heapq import heappush, heappop
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    distance = [[float('INF') for _ in range(N)] for _ in range(N)]
    distance[0][0] = 0
    queue = [(0, 0, 0)]
    while queue:
        cur_weight, cur_x, cur_y = heappop(queue)
        if distance[cur_y][cur_x] < cur_weight:
            continue
        for x, y in direction:
            new_x, new_y = cur_x + x, cur_y + y
            if 0 <= new_x < N and 0 <= new_y < N:
                if grid[new_y][new_x] > grid[cur_y][cur_x]:
                    weight = grid[new_y][new_x] - grid[cur_y][cur_x]
                else:
                    weight = 0
                if distance[new_y][new_x] <= cur_weight + 1 + weight:
                    continue
                distance[new_y][new_x] = cur_weight + 1 + weight
                heappush(queue, (cur_weight + 1 + weight, new_x, new_y))

    print(f'#{t} {distance[N - 1][N - 1]}')