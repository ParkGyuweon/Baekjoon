from collections import defaultdict, deque
N = int(input())
person1, person2 = map(int, input().split())
M = int(input())
graph = defaultdict(list)
visited = [0] * (N + 1)

for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

stack = deque([(person1, 0)])
visited[person1] = 1
cur_flag = False

while stack:
    cur_node, cur_move = stack.popleft()
    if cur_node in graph:
        for item in graph[cur_node]:
            if visited[item] != 1:
                if item == person2:
                    print(cur_move + 1)
                    cur_flag = True
                    break
                stack.append((item, cur_move + 1))
                visited[item] = 1
    if cur_flag:
        break
if not cur_flag:
    print(-1)
