from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)
for idx1 in range(N):
    one_line = list(map(int, input().split()))
    for idx2 in range(N):
        if one_line[idx2] == 1:
            graph[idx1].append(idx2)

answer_grid = [[0 for _ in range(N)] for _ in range(N)]

for item in graph:
    stack = [item]
    visited = []
    visited_grid = [0] * N
    while stack:
        cur_node = stack.pop(0)
        if cur_node in graph:
            for node in graph[cur_node]:
                if not visited_grid[node]:
                    stack.append(node)
                    visited_grid[node] = 1
                    visited.append(node)
    for prev in range(len(visited)):
        answer_grid[item][visited[prev]] = 1

for y in range(len(answer_grid)):
    print(' '.join(map(str, answer_grid[y])))