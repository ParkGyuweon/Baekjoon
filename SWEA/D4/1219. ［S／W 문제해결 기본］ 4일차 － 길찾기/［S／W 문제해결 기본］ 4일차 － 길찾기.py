def find_gil(S, G, current_node):
    while current_node != G:
        for start, dest in node_list:
            if start == current_node:
                if dest == G:
                    return True
                stack.append(dest)
        if not stack:
            return False
        current_node = stack.pop()

for t in range(1, 11):
    test_case, N = map(int, input().split())
    node = list(map(int, input().split()))
    stack, node_list = [], []
    for i in range(0, len(node), 2):
        node_list.append((node[i], node[i + 1]))

    if find_gil(0, 99, 0):
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')