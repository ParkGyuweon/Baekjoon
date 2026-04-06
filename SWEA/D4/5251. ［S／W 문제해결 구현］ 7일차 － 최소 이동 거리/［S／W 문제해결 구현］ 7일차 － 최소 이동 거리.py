from collections import defaultdict
import heapq

T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    bus_fee = defaultdict(list)

    for _ in range(E):
        city1, city2, fee = map(int, input().split())
        bus_fee[city1].append((city2, fee))

    distances = [10E10] * (N + 1)
    distances[0] = 0
    pq = [(0, 0)]
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > distances[current_node]:
            continue
        if current_node in bus_fee:
            for neighbor, fee in bus_fee[current_node]:
                distance = current_dist + fee

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

    print(f'#{t} {distances[N]}')