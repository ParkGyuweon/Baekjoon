from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
min_val = 10E10

N = int(input().strip())
M = int(input().strip())
bus_fee = defaultdict(list)

# 도시 간의 거리를 저장하는 부분(출발 도시, 도착 도시)가 key
for _ in range(M):
    city1, city2, fee = map(int, input().split())
    bus_fee[city1].append((city2, fee))

start_city, end_city = map(int, input().split())
distances = [10E10] * N
distances[start_city - 1] = 0
pq = [(0, start_city)]
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

print(distances[end_city - 1])