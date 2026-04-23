from heapq import heappop, heappush
from collections import defaultdict
graph = defaultdict(list)

N, E = map(int, input().split())
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
node1, node2 = map(int, input().split())

# 시작 -> v1 -> v2 -> 끝
queue = [(0, 1)]
distance = [float('INF') for _ in range(N)]
distance[0] = 0
while queue:
    cur_weight, cur_node = heappop(queue)
    if distance[cur_node - 1] < cur_weight:
        continue
    for weight, node in graph[cur_node]:
        if distance[node - 1] <= cur_weight + weight:
            continue
        distance[node - 1] = cur_weight + weight
        heappush(queue, (cur_weight + weight, node))
start_to_v1 = distance[node1 - 1]
start_to_v2 = distance[node2 - 1]

queue = [(0, N)]
distance = [float('INF') for _ in range(N)]
distance[N - 1] = 0
while queue:
    cur_weight, cur_node = heappop(queue)
    if distance[cur_node - 1] < cur_weight:
        continue
    for weight, node in graph[cur_node]:
        if distance[node - 1] <= cur_weight + weight:
            continue
        distance[node - 1] = cur_weight + weight
        heappush(queue, (cur_weight + weight, node))

v1_to_end = distance[node1 - 1]
v2_to_end = distance[node2 - 1]

queue = [(0, node1)]
distance = [float('INF') for _ in range(N)]
distance[node1 - 1] = 0
while queue:
    cur_weight, cur_node = heappop(queue)
    if distance[cur_node - 1] < cur_weight:
        continue
    for weight, node in graph[cur_node]:
        if distance[node - 1] <= weight + cur_weight:
            continue
        distance[node - 1] = weight + cur_weight
        heappush(queue, (weight + cur_weight, node))

v1_to_v2 = distance[node2 - 1]
v2_to_v1 = distance[node2 - 1]

result = min(start_to_v1 + v1_to_v2 + v2_to_end, start_to_v2 + v2_to_v1 + v1_to_end)
if result == float('INF'):
    print(-1)
else:
    print(result)