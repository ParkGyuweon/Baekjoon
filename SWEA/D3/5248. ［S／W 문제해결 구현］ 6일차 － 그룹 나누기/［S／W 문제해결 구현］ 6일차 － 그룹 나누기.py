T = int(input())

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
        parents[rep_2 - 1] = rep_1
        rank[rep_1 - 1] += 1

for t in range(1, T + 1):
    N, M = map(int, input().split())
    number_list = list(map(int, input().split()))
    parents, rank = make_set(N)
    for i in range(0, len(number_list), 2):
        union_set(number_list[i], number_list[i + 1], parents, rank)

    for node in range(1, N + 1):
        find_set(node, parents)
    print(f'#{t} {len(set(parents))}')