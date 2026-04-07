from heapq import heappush, heappop
from collections import defaultdict

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph[start].append((weight, end))
        graph[end].append((weight, start))

    pq = [(0, 0)]
    MST = [0] * (V + 2)
    min_weight = 0

    while pq:
        cur_weight, cur_node = heappop(pq)

        if MST[cur_node]:
            continue

        MST[cur_node] = 1
        min_weight += cur_weight

        for next_weight, next_node in graph[cur_node]:
            if MST[next_node]:
                continue

            heappush(pq, (next_weight, next_node))

    print(f'#{t} {min_weight}')