from collections import deque
N, K = map(int, input().split())
stack = deque([N])
dist = [-1] * 200001
dist[N] = 0

if N == K:
    print(0)
    exit()
while stack:
    cur_dist = stack.popleft()
    if cur_dist == K:
        print(dist[cur_dist])
        break

    if cur_dist * 2 < 200001 and (dist[cur_dist * 2] == -1 or dist[cur_dist * 2] > dist[cur_dist]):
        stack.appendleft(cur_dist * 2)
        dist[cur_dist * 2] = dist[cur_dist]
    if 0 <= cur_dist - 1 <= 200000 and (dist[cur_dist - 1] == -1 or dist[cur_dist - 1] > dist[cur_dist] + 1):
        stack.append(cur_dist - 1)
        dist[cur_dist - 1] = dist[cur_dist] + 1
    if 0 <= cur_dist + 1 <= 200000 and (dist[cur_dist + 1] == -1 or dist[cur_dist + 1] > dist[cur_dist] + 1):
        stack.append(cur_dist + 1)
        dist[cur_dist + 1] = dist[cur_dist] + 1