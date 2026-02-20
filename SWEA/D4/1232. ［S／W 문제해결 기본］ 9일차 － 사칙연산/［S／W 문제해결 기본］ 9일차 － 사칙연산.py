def calc(node):
    if node not in tree:
        return int(character[node - 1])
    if character[node - 1] == '+':
        return calc(tree[node][0]) + calc(tree[node][1])
    elif character[node - 1] == '-':
        return calc(tree[node][0]) - calc(tree[node][1])
    elif character[node - 1] == '*':
        return calc(tree[node][0]) * calc(tree[node][1])
    elif character[node - 1] == '/':
        return calc(tree[node][0]) / calc(tree[node][1])

for t in range(1, 11):
    N = int(input())
    tree = {}
    character = [0] * N

    for i in range(N):
        one_line = list(input().split())
        if len(one_line) == 4:
            tree[int(one_line[0])] = list(map(int, one_line[2:]))
        character[int(one_line[0]) - 1] = one_line[1]
    print(f'#{t} {int(calc(1))}')



