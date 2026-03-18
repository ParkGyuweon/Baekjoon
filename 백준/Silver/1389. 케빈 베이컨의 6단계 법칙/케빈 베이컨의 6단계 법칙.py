from collections import defaultdict
N, M = map(int, input().split())
graph = defaultdict(list)
bacon = {}
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

def bfs(friend):
    stack = [(friend, 0)]
    visited = [0] * N
    while stack:
        cur_position, cur_time = stack.pop(0)
        for item in graph[cur_position]:
            if not visited[item - 1]:
                stack.append((item, cur_time + 1))
                visited[item - 1] = cur_time + 1
    return sum(visited)

friend_list = [0] * N
min_val = 10E10
result = 0
for friend in range(1, N + 1):
    cur_val = bfs(friend)
    if cur_val < min_val:
        min_val = cur_val
        result = friend
    elif cur_val == min_val and friend < result:
        result = friend

print(result)