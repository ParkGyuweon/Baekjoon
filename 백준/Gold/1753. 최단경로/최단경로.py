from heapq import heappop, heappush
from collections import defaultdict
V, E = map(int, input().split())
start_node = int(input())
graph = defaultdict(list)
for _ in range(E):
    node1, node2, weight = map(int, input().split())
    graph[node1].append((weight, node2))

queue = [(0, start_node)]
distance = [float('INF') for _ in range(V)]
distance[start_node - 1] = 0
while queue:
    cur_weight, cur_node = heappop(queue)
    if distance[cur_node - 1] < cur_weight:
        continue

    for weight, node in graph[cur_node]:
        if distance[node - 1] <= cur_weight + weight:
            continue
        distance[node - 1] = cur_weight + weight
        heappush(queue, (cur_weight + weight, node))

for item in distance:
    if item == float('INF'):
        print('INF')
    else:
        print(item)

