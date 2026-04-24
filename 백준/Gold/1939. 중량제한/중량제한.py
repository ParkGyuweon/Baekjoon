N, M = map(int, input().split())
def make_set(N):
    parents = [i + 1 for i in range(N)]
    rank = [0 for i in range(N)]
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
        parents[rep_2 - 1] = rep_1
        rank[rep_1 - 1] += 1

parents, rank = make_set(N)
graph = [tuple(map(int, input().split())) for _ in range(M)]
graph.sort(key=lambda x:-x[2])
start, end = map(int, input().split())

for node1, node2, weight in graph:
    if find_set(node1, parents) != find_set(node2, parents):
        union_set(node1, node2, parents, rank)
        if find_set(start, parents) == find_set(end, parents):
            print(weight)
            break
