from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

N, E = map(int, input().split())
bus_fee = defaultdict(list)

for _ in range(E):
    city1, city2, fee = map(int, input().split())
    bus_fee[city1].append((city2, fee))
    bus_fee[city2].append((city1, fee))

node1, node2 = map(int, input().split())

def two_node(start_node, end_node):
    pq = [(0, start_node)]
    distances = [10E10] * N
    distances[start_node - 1] = 0
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > distances[current_node - 1]:
            continue

        if current_node in bus_fee:
            for neighbor, fee in bus_fee[current_node]:
                distance = current_dist + fee

                if distance < distances[neighbor - 1]:
                    distances[neighbor - 1] = distance
                    heapq.heappush(pq, (distance, neighbor))

    return distances[end_node - 1]

result = min(two_node(1, node1) + two_node(node1, node2) + two_node(node2, N), two_node(1, node2) + two_node(node2, node1) + two_node(node1, N))
if result >= 10E10:
    print(-1)
else:
    print(result)