from collections import deque
from heapq import heappush, heappop
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def restore_bfs():
    distances = [[10E10 for _ in range(N)] for _ in range(N)]
    distances[0][0] = 0
    stack = [[0, 0, 0]]
    while stack:
        cur_dist, cur_x, cur_y = heappop(stack)
        if cur_dist > distances[cur_y][cur_x]:
            continue
        for x, y in direction:
            new_x, new_y = cur_x + x, cur_y + y
            if 0 <= new_x < N and 0 <= new_y < N:
                distance = cur_dist + grid[new_y][new_x]

                if distance < distances[new_y][new_x]:
                    distances[new_y][new_x] = distance
                    heappush(stack, (distance, new_x, new_y))

    return distances[N - 1][N - 1]

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, list(input()))) for _ in range(N)]
    result = restore_bfs()
    print(f'#{t} {result}')