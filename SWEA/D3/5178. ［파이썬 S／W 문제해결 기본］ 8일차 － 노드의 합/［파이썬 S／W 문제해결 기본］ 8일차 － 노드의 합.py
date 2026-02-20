T = int(input())

def calc(tree, node):
    if tree[node] != 0:
        return tree[node]
    if node * 2 <= N and node * 2 + 1 <= N:
        tree[node] = calc(tree, node * 2) + calc(tree, node * 2 + 1)
    elif node * 2 <= N:
        tree[node] = calc(tree, node * 2)
    return tree[node]

for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for i in range(M):
        node, num = map(int, input().split())
        tree[node] = num
    calc(tree, 1)
    print(f'#{t} {tree[L]}')

