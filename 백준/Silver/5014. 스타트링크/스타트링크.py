from collections import deque
F, S, G, U, D = map(int, input().split())
stack = deque([(S, 0)])
visited = [0] * (F + 1)
visited[S] = 1
if S == G:
    print(0)
else:
    while stack:
        cur_num, cur_move = stack.popleft()
        if cur_num + U <= F and visited[cur_num + U] == 0:
            if cur_num + U == G:
                print(cur_move + 1)
                break
            visited[cur_num + U] = 1
            stack.append((cur_num + U, cur_move + 1))
    
        if 1 <= cur_num - D and visited[cur_num - D] == 0:
            if cur_num - D == G:
                print(cur_move + 1)
                break
            visited[cur_num - D] = 1
            stack.append((cur_num - D, cur_move + 1))
    else:
        print('use the stairs')
