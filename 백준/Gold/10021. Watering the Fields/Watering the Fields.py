from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N, C = map(int, input().split())
position = [list(map(int, input().split())) for _ in range(N)]

min_dist = [float('inf')] * N
visited = [False] * N

queue = [(0, 0)] 
min_dist[0] = 0
min_weight = 0
cnt = 0

while queue:
    cur_w, cur_n = heappop(queue)

    if visited[cur_n]:
        continue

    if cur_w > min_dist[cur_n]:
        continue

    visited[cur_n] = True
    min_weight += cur_w
    cnt += 1

    if cnt == N:
        break

    curr_x, curr_y = position[cur_n]
    for nxt_n in range(N):
        if not visited[nxt_n]:
            nxt_x, nxt_y = position[nxt_n]
            dist = (curr_x - nxt_x) ** 2 + (curr_y - nxt_y) ** 2

            if dist >= C and dist < min_dist[nxt_n]:
                min_dist[nxt_n] = dist
                heappush(queue, (dist, nxt_n))

if cnt == N:
    print(min_weight)
else:
    print(-1)