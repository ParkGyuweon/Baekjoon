from collections import defaultdict, deque
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    visited = [0] * (N + 1)
    stack = deque()
    for node in range(1, N + 1):
        new_visited = visited[:]
        new_visited[node] = 1
        stack.append((node, 1, new_visited))

    max_move = 0
    while stack:
        cur_node, cur_move, cur_visited = stack.popleft()
        max_move = max(max_move, cur_move)
        if cur_node in graph:
            for item in graph[cur_node]:
                if cur_visited[item] == 0:
                    new_visited = cur_visited[:]
                    new_visited[item] = 1
                    stack.append((item, cur_move + 1, new_visited))

    print(f'#{t} {max_move}')