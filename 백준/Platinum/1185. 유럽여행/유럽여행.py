from heapq import heappop, heappush
from collections import defaultdict
import sys
input = sys.stdin.readline

N, P = map(int, input().split())
country_cost = [int(input().strip()) for _ in range(N)]
graph = defaultdict(list)
for _ in range(P):
    node1, node2, weight = map(int, input().split())
    graph[node1].append((weight, node2))
    graph[node2].append((weight, node1))

start = country_cost.index(min(country_cost)) + 1
queue = [(0, start)]
visited = [0] * N
min_weight = country_cost[start - 1]

while queue:
    cur_weight, cur_node = heappop(queue)
    if visited[cur_node - 1]:
        continue

    visited[cur_node - 1] = 1
    min_weight += cur_weight
    for weight, node in graph[cur_node]:
        if visited[node - 1]:
            continue
        heappush(queue, (2 * weight + country_cost[node - 1] + country_cost[cur_node - 1], node))

print(min_weight)