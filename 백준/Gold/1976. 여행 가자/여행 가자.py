N = int(input())
M = int(input())

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
    elif rank[rep_2] < rank[rep_1]:
        parents[rep_2] = rep_1
    else:
        parents[rep_1] = rep_2
        rank[rep_2] += 1
parents, rank = make_set(N)
grid = [list(map(int, input().split())) for _ in range(N)]
for y in range(N):
    for x in range(N):
        if grid[y][x] == 1:
            union_set(x, y, parents, rank)

number_list = list(map(int, input().split()))
if M > 0:
    answer = find_set(number_list[0] - 1, parents)
for item in number_list:
    if find_set(item - 1, parents) != answer:
        print('NO')
        break
else:
    print('YES')