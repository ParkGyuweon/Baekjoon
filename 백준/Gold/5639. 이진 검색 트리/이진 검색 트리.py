from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
nodes = deque()
graph = defaultdict(list)

while True:
    try:
        node = int(input().strip())
        nodes.append(node)
    except:
        break
root = nodes.popleft()

def tree(node, nodes):
    if len(nodes) == 0:
        return

    left_child, right_child = deque(), deque()
    while nodes:
        item = nodes.popleft()
        if item > node:
            right_child.append(item)
        else:
            left_child.append(item)
    if left_child:
        left = left_child.popleft()
        graph[node] = [left]
        tree(left, left_child)
    if right_child:
        right = right_child.popleft()
        graph[node].append(right)
        tree(right, right_child)
tree(root, nodes)

def postfix(node):
    global answer
    if node not in graph:
        print(node)
        return
    if len(graph[node]) == 1:
        postfix(graph[node][0])
        print(node)
        return
    if len(graph[node]) == 2:
        postfix(graph[node][0])
        postfix(graph[node][1])
        print(node)
        return
postfix(root)