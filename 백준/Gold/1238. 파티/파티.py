from heapq import heappop, heappush
from collections import defaultdict

N, M, X = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    start, end, T = map(int, input().split())
    graph[start].append((T, end))

going = [0] * N
for student in range(1, N + 1):
    queue = [(0, student)]
    distance = [float('INF') for _ in range(N)]
    distance[student - 1] = 0
    while queue:
        cur_weight, cur_node = heappop(queue)
        if distance[cur_node - 1] < cur_weight:
            continue

        for weight, node in graph[cur_node]:
            if distance[node - 1] <= cur_weight + weight:
                continue
            distance[node - 1] = cur_weight + weight
            heappush(queue, (cur_weight + weight, node))

    going[student - 1] = distance[X - 1]

queue = [(0, X)]
distance = [float('INF') for _ in range(N)]
distance[X - 1] = 0
while queue:
    cur_weight, cur_node = heappop(queue)
    if distance[cur_node - 1] < cur_weight:
        continue
    for weight, node in graph[cur_node]:
        if distance[node - 1] <= cur_weight + weight:
            continue
        distance[node - 1] = cur_weight + weight
        heappush(queue, (cur_weight + weight, node))

for student in range(N):
    distance[student] += going[student]

print(max(distance))