from heapq import heappop, heappush
from collections import defaultdict

graph = defaultdict(list)
N, M = map(int, input().split())
W_set = set()
M_set = set()
school_list = list(input().split())

for num in range(1, N + 1):
    if school_list[num - 1] == 'W':
        W_set.add(num)
    elif school_list[num - 1] == 'M':
        M_set.add(num)

for _ in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end))
    graph[end].append((weight, start))

queue = [(0, 1)]
min_weight = 0
visited = [0] * N
while queue:
    cur_weight, cur_node = heappop(queue)
    if visited[cur_node - 1]:
        continue
    visited[cur_node - 1] = 1
    min_weight += cur_weight
    for weight, node in graph[cur_node]:
        if visited[node - 1] or (cur_node in W_set and node in W_set) or (cur_node in M_set and node in M_set):
            continue
        heappush(queue, (weight, node))

if sum(visited) == N:
    print(min_weight)
else:
    print(-1)