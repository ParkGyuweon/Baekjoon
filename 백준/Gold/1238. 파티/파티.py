from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
bus_fee = defaultdict(list)

for _ in range(M):
    city1, city2, fee = map(int, input().split())
    bus_fee[city1].append((city2, fee))

def two_node(node):
    distances = [10E10] * N
    distances[node - 1] = 0
    pq = [(0, node)]
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
    return distances

answer = [0] * N
max_val = 0
for n in range(1, N + 1):
    answer[n - 1] = two_node(n)[X - 1]
answer_2 = two_node(X)
for n in range(N):
    max_val = max(max_val, answer[n] + answer_2[n])
print(max_val)