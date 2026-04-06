from collections import defaultdict, deque
T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    graph = defaultdict(list)
    one_line = list(map(int, input().split()))
    for i in range(0, len(one_line), 2):
        graph[one_line[i]].append(one_line[i + 1])
    start, end = map(int, input().split())
    visited = [0] * N
    visited[start - 1] = 1
    stack = deque([[start, visited]])
    answer = 0
    while stack:
        cur_node, cur_visited = stack.popleft()
        if cur_node in graph:
            for item in graph[cur_node]:
                if item == end:
                    answer += 1
                    continue
                if cur_visited[item - 1] == 0:
                    new_visited = cur_visited[:]
                    new_visited[item - 1] = 1
                    stack.append([item, new_visited])
    print(f'#{t} {answer}')