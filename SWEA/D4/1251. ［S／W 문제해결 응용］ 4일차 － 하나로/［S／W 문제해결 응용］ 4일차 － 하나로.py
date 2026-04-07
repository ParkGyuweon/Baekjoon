from heapq import heappush, heappop
def bridge(start_island):
    pq = [(0, start_island)]
    MST = [0] * N
    min_weight = 0

    while pq:
        weight, node = heappop(pq)

        if MST[node]:
            continue

        MST[node] = 1
        min_weight += weight ** 2

        for next_weight, next_node in graph[node]:
            if MST[next_node]:
                continue

            heappush(pq, (next_weight, next_node))

    return min_weight

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    graph = [[] * N for _ in range(N)]
    island = []
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    for node in range(N):
        x, y = x_list[node], y_list[node]
        for idx in range(len(island)):
            item = island[idx]
            graph[len(island)].append((((item[0] - x) ** 2 + (item[1] - y) ** 2) ** (1/2), idx))
            graph[idx].append((((item[0] - x) ** 2 + (item[1] - y) ** 2) ** (1 / 2), len(island)))
        island.append((x, y))

    E = float(input())
    result = bridge(0) * E
    if result - int(result) >= 0.5:
        print(f'#{t} {int(result) + 1}')
    else:
        print(f'#{t} {int(result)}')
