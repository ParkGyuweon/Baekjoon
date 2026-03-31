from collections import defaultdict
import heapq, sys
input = sys.stdin.readline
V, E = map(int, input().split())
start_node = int(input().strip())
graph = defaultdict(list)

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))

distances = ['INF'] * V
distances[start_node - 1] = 0
pq = [(0, start_node)]
while pq:
    cur_dist, cur_node = heapq.heappop(pq)
    if cur_dist > float(distances[cur_node - 1]):
        continue
    if cur_node in graph:
        for neighbor, fee in graph[cur_node]:
            distance = cur_dist + fee

            if distance < float(distances[neighbor - 1]):
                distances[neighbor - 1] = distance
                heapq.heappush(pq, (distance, neighbor))

print('\n'.join(map(str, distances)))