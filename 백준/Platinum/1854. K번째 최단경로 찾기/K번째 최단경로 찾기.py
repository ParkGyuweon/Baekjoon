from heapq import heappop, heappush
from collections import defaultdict

N, M, K = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    node1, node2, weight = map(int, input().split())
    graph[node1].append((weight, node2))

queue = [(0, 1)]
distance = [[] for _ in range(N)]
heappush(distance[0], 0)

while queue:
    cur_weight, cur_node = heappop(queue)

    for weight, node in graph[cur_node]:
        if len(distance[node - 1]) < K:
            heappush(distance[node - 1], (cur_weight + weight) * -1)
            heappush(queue, (weight + cur_weight, node))
        elif -1 * distance[node - 1][0] > cur_weight + weight:
            heappop(distance[node - 1])
            heappush(distance[node - 1], (cur_weight + weight) * -1)
            heappush(queue, (weight + cur_weight, node))

for item in distance:
    if len(item) < K:
        print(-1)
    else:
        print(heappop(item) * -1)

