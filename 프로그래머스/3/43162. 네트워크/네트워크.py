def make_set(N):
    parents = [i for i in range(N)]
    rank = [0] * N
    return parents, rank

def find_set(node, parents):
    if parents[node] == node:
        return node
    parents[node] = find_set(parents[node], parents)
    return parents[node]

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
        parents[rep_2] = rep_1
        rank[rep_1] += 1

def solution(n, computers):
    parents, rank = make_set(n)
    for y in range(n):
        for x in range(n):
            if computers[y][x] == 1:
                union_set(x, y, parents, rank)
    for item in range(n):
        find_set(item, parents)
    
    return len(set(parents))