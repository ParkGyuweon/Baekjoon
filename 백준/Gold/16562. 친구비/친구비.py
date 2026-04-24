N, M, K = map(int, input().split())
money_list = list(map(int, input().split()))

def make_set(N):
    parents = [i + 1 for i in range(N)]
    return parents

def find_set(node, parents):
    if parents[node - 1] == node:
        return node
    parents[node - 1] = find_set(parents[node - 1], parents)
    return parents[node - 1]

def union_set(node1, node2, parents, money_list):
    rep_1 = find_set(node1, parents)
    rep_2 = find_set(node2, parents)

    if rep_1 == rep_2:
        return

    if money_list[rep_1 - 1] > money_list[rep_2 - 1]:
        parents[rep_1 - 1] = rep_2
    elif money_list[rep_1 - 1] < money_list[rep_2 - 1]:
        parents[rep_2 - 1] = rep_1
    else:
        if rep_1 < rep_2:
            parents[rep_2 - 1] = rep_1
        else:
            parents[rep_1 - 1] = rep_2

parents = make_set(N)
for _ in range(M):
    person1, person2 = map(int, input().split())
    union_set(person1, person2, parents, money_list)

for node in range(1, N + 1):
    find_set(node, parents)
    
sum_val = 0
for item in set(parents):
    sum_val += money_list[item - 1]
if sum_val <= K:
    print(sum_val)
else:
    print('Oh no')