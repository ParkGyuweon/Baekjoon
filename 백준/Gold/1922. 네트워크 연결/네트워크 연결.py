from heapq import heappop, heappush
from collections import defaultdict

N = int(input())
M = int(input())
graph = defaultdict(list)
for _ in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end))
    graph[end].append((weight, start))

queue = [(0, 1)]
visited = [0]* N
min_weight = 0
while queue:
    cur_weight, cur_node = heappop(queue)
    if visited[cur_node - 1]:
        continue

    visited[cur_node - 1] = 1
    min_weight += cur_weight

    for weight, node in graph[cur_node]:
        if visited[node - 1]:
            continue
        heappush(queue, (weight, node))

print(min_weight)