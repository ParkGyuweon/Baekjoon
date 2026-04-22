G = int(input())
P = int(input())

def make_set(G):
    parents = [i for i in range(G + 1)]
    rank = [0] * (G + 1)
    return parents, rank

def find_set(node, parents):
    if parents[node] == node:
        return node
    parents[node] = find_set(parents[node], parents)
    return parents[node]

def union_set(node1, node2, parents, rank, flag):
    global result
    rep_1 = find_set(node1, parents)
    rep_2 = find_set(node2, parents)
    if rep_1 == rep_2:
        return
    result += 1
    if rep_1 < rep_2:
        parents[rep_2] = rep_1
    elif rep_2 < rep_1:
        parents[rep_1] = rep_2

    return flag

result = 0
parents, rank = make_set(G)
for _ in range(P):
    gate = int(input())
    cur_site = find_set(gate, parents)
    if cur_site != 0:
        union_set(cur_site, cur_site - 1, parents, rank, False)
    else:
        break
print(result)
