from collections import defaultdict

N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

connected_num = 0
visited = [0] * (N + 1)

for item in graph:
    if visited[item] == 0:
        stack = [item]
        while stack:
            cur_node = stack.pop()
            if cur_node in graph:
                for item in graph[cur_node]:
                    if visited[item] == 0:
                        stack.append(item)
                        visited[item] = 1
        connected_num += 1

print(connected_num + visited.count(0) - 1)