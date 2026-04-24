from heapq import heappush, heappop
from collections import defaultdict

T = int(input())
for t in range(1, T + 1):
    N, D, C = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(D):
        node1, node2, weight = map(int, input().split())
        graph[node2].append((weight, node1))

    queue = [(0, C)]
    distance = [float('INF') for _ in range(N)]
    distance[C - 1] = 0
    while queue:
        cur_weight, cur_node = heappop(queue)
        if distance[cur_node - 1] < cur_weight:
            continue

        for weight, node in graph[cur_node]:
            if distance[node - 1] <= cur_weight + weight:
                continue
            distance[node - 1] = cur_weight + weight
            heappush(queue, (weight + cur_weight, node))
    max_idx, max_number = 0, 0
    for num in range(len(distance)):
        if distance[num] != float('INF'):
            max_idx += 1
            max_number = max(max_number, distance[num])

    print(max_idx, max_number)