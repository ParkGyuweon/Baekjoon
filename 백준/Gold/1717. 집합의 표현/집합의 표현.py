N, M = map(int, input().split())
def make_set(N):
    parents = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    return parents, rank

def find_set(node, parents):
    if parents[node] == node:
        return node
    return find_set(parents[node], parents)

def union_set(node1, node2, parents, rank):
    rep_1 = find_set(node1, parents)
    rep_2 = find_set(node2, parents)

    if rep_1 == rep_2:
        return
    if rank[rep_1] < rank[rep_2]:
        parents[rep_1] = rep_2
    elif rank[rep_1] > rank[rep_2]:
        parents[rep_2] = rep_1
    else:
        parents[rep_1] = rep_2
        rank[rep_2] += 1

parents, rank = make_set(N)

for _ in range(M):
    number, set1, set2 = map(int, input().split())
    if number == 0:
        union_set(set1, set2, parents, rank)
    else:
        if find_set(set1, parents) == find_set(set2, parents):
            print('YES')
        else:
            print('NO')
