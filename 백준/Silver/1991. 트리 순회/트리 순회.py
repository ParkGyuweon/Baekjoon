N = int(input())
graph = {}

for _ in range(N):
    one_line = list(input().split())
    graph[one_line[0]] = [one_line[1], one_line[2]]

def preorder_traversel(node):
    if node not in graph:
        return ''
    left = preorder_traversel(graph[node][0])
    right = preorder_traversel(graph[node][1])
    return node + left + right

def inorder_traversal(node):
    if node not in graph:
        return ''
    left = inorder_traversal(graph[node][0])
    right = inorder_traversal(graph[node][1])
    return left + node + right

def postorder_traversal(node):
    if node not in graph:
        return ''
    left = postorder_traversal(graph[node][0])
    right = postorder_traversal(graph[node][1])
    return left + right + node

print(preorder_traversel('A'))
print(inorder_traversal('A'))
print(postorder_traversal('A'))