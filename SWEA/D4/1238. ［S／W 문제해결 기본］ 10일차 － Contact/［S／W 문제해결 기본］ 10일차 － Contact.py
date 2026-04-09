from collections import defaultdict, deque
for t in range(1, 11):
    N, S = map(int, input().split())
    graph = defaultdict(list)
    numbers = list(map(int, input().split()))
    for idx in range(0, len(numbers), 2):
        graph[numbers[idx]].append(numbers[idx + 1])
    stack = deque([(S, 0)])
    max_move, max_number = 0, 0
    visited = {S}
    while stack:
        cur_node, cur_move = stack.popleft()
        if cur_move > max_move:
            max_move = cur_move
            max_number = cur_node
        elif cur_move == max_move:
            max_number = max(max_number, cur_node)

        if cur_node in graph:
            for item in graph[cur_node]:
                if item not in visited:
                    stack.append((item, cur_move + 1))
                    visited.add(item)

    print(f'#{t} {max_number}')