from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N = int(input())
bus_fee = defaultdict(list)

for _ in range(N):
    one_line = list(map(int, input().split()))[:-1]
    for idx in range(1, len(one_line), 2):
        bus_fee[one_line[0]].append((one_line[idx], one_line[idx + 1]))
        bus_fee[one_line[idx]].append((one_line[0], one_line[idx + 1]))

def two_node(node):
    distances = [-1] * (N + 1)
    distances[node] = 0
    stack = deque([node])

    max_node = node
    max_dist = 0

    while stack:
        current_node = stack.popleft()

        for neighbor, fee in bus_fee[current_node]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current_node] + fee
                stack.append(neighbor)

                if distances[neighbor] > max_dist:
                    max_dist = distances[neighbor]
                    max_node = neighbor
    return max_node, max_dist

if N == 1:
    print(0)
else:
    node_a, dist_a = two_node(1)
    node_b, dist_b = two_node(node_a)

    print(dist_b)