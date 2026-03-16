from collections import defaultdict

N = int(input())
graph = defaultdict(list)

for _ in range(N - 1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

number_list = [0] * (N + 1)
stack = [1]
while stack:
    cur_node = stack.pop(0)
    if cur_node in graph:
        for item in graph[cur_node]:
            if number_list[item] == 0:
                number_list[item] = cur_node
                stack.append(item)

for i in range(2, N + 1):
    print(number_list[i])