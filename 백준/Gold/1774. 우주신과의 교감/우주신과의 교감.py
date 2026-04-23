from heapq import heappop, heappush
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP

N, M = map(int, input().split())
position = {}
graph = defaultdict(list)

for got in range(N):
    x, y = map(int, input().split())
    for key, value in position.items():
        distance = ((value[0] - x) ** 2 + (value[1] - y) ** 2) ** (1/2)
        graph[key].append((distance, got))
        graph[got].append((distance, key))
    position[got] = (x, y)

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1 - 1].append((0, node2 - 1))
    graph[node2 - 1].append((0, node1 - 1))

queue = [(0, 0)]
visited = [0] * N
min_weight = 0

while queue:
    cur_weight, cur_node = heappop(queue)
    if visited[cur_node]:
        continue

    visited[cur_node] = 1
    min_weight += cur_weight
    for weight, node in graph[cur_node]:
        if visited[node]:
            continue
        heappush(queue, (weight, node))

result = Decimal(min_weight).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print(result)
