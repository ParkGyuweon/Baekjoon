from heapq import heappop, heappush
from collections import defaultdict

N = int(input())
M = int(input())
graph = defaultdict(list)
for _ in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end))

start_node, end_node = map(int, input().split())

queue = [(0, start_node)]
distance = [float('INF') for _ in range(N)]
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

print(distance[end_node - 1])