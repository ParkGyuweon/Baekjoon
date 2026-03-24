import sys
input = sys.stdin.readline
from collections import defaultdict

N, M, R = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for key, value in graph.items():
    value.sort()

stack = [R]
visited = [0] * (N + 1)
visited[R] = 1
cur_num = 1
answer_list = [0] * (N + 1)

while stack:
    cur_node = stack.pop(0)
    answer_list[cur_node] = cur_num
    cur_num += 1
    if cur_node in graph:
        for item in range(len(graph[cur_node])):
            if visited[graph[cur_node][item]] == 0:
                stack.append(graph[cur_node][item])
                visited[graph[cur_node][item]] = 1
print('\n'.join(map(str, answer_list[1:])))
