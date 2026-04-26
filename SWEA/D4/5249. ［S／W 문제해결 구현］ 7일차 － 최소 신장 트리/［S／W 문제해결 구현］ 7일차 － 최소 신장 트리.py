from heapq import heappop, heappush
from collections import defaultdict
T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        node1, node2, weight = map(int, input().split())
        graph[node1].append((weight, node2))
        graph[node2].append((weight, node1))

    visited = [0] * (V + 1)
    min_weight = 0
    queue = [(0, 0)]
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
    print(f'#{t} {min_weight}')