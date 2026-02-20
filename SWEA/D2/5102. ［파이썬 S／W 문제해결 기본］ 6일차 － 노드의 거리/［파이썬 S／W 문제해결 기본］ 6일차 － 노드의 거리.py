from collections import defaultdict

T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for i in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    S, G = map(int, input().split())
    
    def bfs(S, G, graph):
        stack = [(S, 0)]
        visited = []
        while stack:
            current, time = stack.pop(0)
            visited.append(current)
            for item in graph[current]:
                if item not in visited:
                    stack.append((item, time + 1))
                if item == G:
                    return time + 1
                
    result = bfs(S, G, graph)        
    if result == None:
        print(f'#{t} 0')
    else:
    	print(f'#{t} {result}')