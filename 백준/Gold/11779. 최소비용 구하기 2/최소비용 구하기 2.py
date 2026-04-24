from heapq import heappop, heappush
from collections import defaultdict

N = int(input())
M = int(input())
graph = defaultdict(list)
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))

start, end = map(int, input().split())
queue = [(0, start, [start])]
distance = [float('INF') for _ in range(N)]
distance[start - 1] = 0
answer = 0
while queue:
    cur_weight, cur_node, cur_path = heappop(queue)
    if distance[cur_node - 1] < cur_weight:
        continue
    for weight, node in graph[cur_node]:
        if distance[node - 1] <= cur_weight + weight:
            continue
        distance[node - 1] = cur_weight + weight
        if node == end:
            answer = cur_path + [node]
        heappush(queue, (weight + cur_weight, node, cur_path + [node]))

print(distance[end - 1])
print(len(answer))
print(' '.join(map(str, answer)))

