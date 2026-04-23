from collections import defaultdict

N = int(input())
M = int(input())
edges = [tuple(map(int, input().split())) for _ in range(M)]
edges.sort(key=lambda x:x[2])

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
    if rep_2 == rep_1:
        return
    if rank[rep_1 - 1] < rank[rep_2 - 1]:
        parents[rep_1 - 1] = rep_2
    elif rank[rep_1 - 1] > rank[rep_2 - 1]:
        parents[rep_2 - 1] = rep_1
    else:
        parents[rep_2 - 1] = rep_1
        rank[rep_1 - 1] += 1

parents, rank = make_set(N)
min_weight = 0
for s, e, w in edges:
    if find_set(s, parents) != find_set(e, parents):
        union_set(s, e, parents, rank)
        min_weight += w

print(min_weight)