T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    node_list = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    stack, current_node = [], S
    
    while current_node != G:
        for start, dest in node_list:
            if start == current_node:
                stack.append(dest)
        if not stack or current_node == G:
            break
        current_node = stack.pop()
        
    if current_node == G:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')