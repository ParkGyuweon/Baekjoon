T = int(input())

for t in range(1, T + 1):
    E, N = map(int, input().split())
    numbers = list(map(int, input().split()))
    node = []
    for i in range(len(numbers) // 2):
        node.append((numbers[2 * i], numbers[2 * i + 1]))
    node_num, stack = 0, [N]
    while stack:
        current = stack.pop(0)
        node_num += 1
        for item in node:
            if item[0] == current:
                stack.append(item[1])

    print(f'#{t} {node_num}')