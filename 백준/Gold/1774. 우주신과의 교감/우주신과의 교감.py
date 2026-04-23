N, M = map(int, input().split())
from decimal import Decimal, ROUND_HALF_UP

def make_set(N):
    parents = [i + 1 for i in range(N)]
    rank = [0] * N
    return parents, rank

def find_set(node, parents):
    if parents[node - 1] == node:
        return node

    parents[node - 1] = find_set(parents[node - 1], parents)
    return parents[node - 1]

def union_set(node1, node2, parents, rank):
    rep_1 = find_set(node1, parents)
    rep_2 = find_set(node2, parents)
    if rep_1 == rep_2:
        return
    if rank[rep_1 - 1] < rank[rep_2 - 1]:
        parents[rep_1 - 1] = rep_2
    elif rank[rep_1 - 1] > rank[rep_2 - 1]:
        parents[rep_2 - 1] = rep_1
    else:
        parents[rep_1 - 1] = rep_2
        rank[rep_2 - 1] += 1

position = []
graph = []
for i in range(1, N + 1):
    x, y = map(int, input().split())
    for num in range(len(position)):
        item = position[num]
        distance = ((item[0] - x) ** 2 + (item[1] - y) ** 2) ** (1/2)
        graph.append((i, num + 1, distance))
    position.append((x, y))
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph.append((node1, node2, 0))
graph.sort(key=lambda x:x[2])
parents, rank = make_set(N)
min_weight = 0
for s, e, w in graph:
    if find_set(s, parents) != find_set(e, parents):
        union_set(s, e, parents, rank)
        min_weight += w

result = Decimal(min_weight).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print(result)