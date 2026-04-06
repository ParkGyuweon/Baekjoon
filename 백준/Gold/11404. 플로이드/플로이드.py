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

distances = [[10E10 for _ in range(N)] for _ in range(N)]

pq = [(0, city, city) for city in range(1, N + 1)]
while pq:
    current_dist, current_node, start_node = heapq.heappop(pq)
    if current_dist > distances[start_node - 1][current_node - 1]:
        continue
    if current_node in bus_fee:
        for neighbor, fee in bus_fee[current_node]:
            distance = current_dist + fee

            if distance < distances[start_node - 1][neighbor - 1]:
                distances[start_node - 1][neighbor - 1] = distance
                heapq.heappush(pq, (distance, neighbor, start_node))

for first_city in range(N):
    for second_city in range(N):
        if distances[first_city][second_city] == 10E10:
            distances[first_city][second_city] = 0
        if first_city == second_city:
            distances[first_city][second_city] = 0
            
for y in range(N):
    print(' '.join(map(str, distances[y])))