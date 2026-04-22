T = int(input())

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
        count[rep_2] += count[rep_1]
    elif rank[rep_1] > rank[rep_2]:
        parents[rep_2] = rep_1
        count[rep_1] += count[rep_2]
    else:
        parents[rep_2] = rep_1
        rank[rep_1] += 1
        count[rep_1] += count[rep_2]

for t in range(1, T + 1):
    friends_dict = {}
    current_number = 0
    parents = []
    rank = []
    count = []
    F = int(input())
    for _ in range(F):
        person1, person2 = input().split()
        if person1 not in friends_dict:
            friends_dict[person1] = current_number
            parents.append(current_number)
            rank.append(0)
            current_number += 1
            count.append(1)
        if person2 not in friends_dict:
            friends_dict[person2] = current_number
            parents.append(current_number)
            rank.append(0)
            current_number += 1
            count.append(1)
        union_set(friends_dict[person1], friends_dict[person2], parents, rank)
        print(count[find_set(friends_dict[person1], parents)])

