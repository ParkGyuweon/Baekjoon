N = int(input())
position = []
for item1 in range(1, N + 1):
    x, y, z = map(int, input().split())
    position.append((x, y, z, item1))

x_position = sorted(position, key=lambda x:x[0])
y_position = sorted(position, key=lambda x:x[1])
z_position = sorted(position, key=lambda x:x[2])
graph = []

for idx in range(N - 1):
    graph.append((x_position[idx][3], x_position[idx + 1][3], abs(x_position[idx][0] - x_position[idx + 1][0])))
    graph.append((y_position[idx][3], y_position[idx + 1][3], abs(y_position[idx][1] - y_position[idx + 1][1])))
    graph.append((z_position[idx][3], z_position[idx + 1][3], abs(z_position[idx][2] - z_position[idx + 1][2])))

graph.sort(key=lambda x:x[2])

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

    if rank[rep_2 - 1] > rank[rep_1 - 1]:
        parents[rep_1 - 1] = rep_2
    elif rank[rep_2 - 1] < rank[rep_1 - 1]:
        parents[rep_2 - 1] = rep_1
    else:
        parents[rep_2 - 1] = rep_1
        rank[rep_1 - 1] += 1

parents, rank = make_set(N)
min_weight = 0
for node1, node2, weight in graph:
    if find_set(node1, parents) != find_set(node2, parents):
        union_set(node1, node2, parents, rank)
        min_weight += weight

print(min_weight)