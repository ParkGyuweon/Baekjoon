from collections import deque

N, K = map(int, input().split())
if N == K:
    print(0)
else:
    visited = [0] * 200000
    stack = deque([(N, 0)])
    while stack:
        cur_position, cur_time = stack.popleft()
        if cur_position * 2 == K or cur_position - 1 == K or cur_position + 1 == K:
            print(cur_time + 1)
            break
        if cur_position <= K:
            if 0 <= cur_position * 2 < 200000 and visited[cur_position * 2] == 0:
                stack.append((cur_position * 2, cur_time + 1))
                visited[cur_position * 2] = 1
            if 0 <= cur_position + 1 < 200000 and visited[cur_position + 1] == 0:
                stack.append((cur_position + 1, cur_time + 1))
                visited[cur_position + 1] = 1
            if 0 <= cur_position - 1 < 200000 and visited[cur_position - 1] == 0:
                stack.append((cur_position - 1, cur_time + 1))
                visited[cur_position - 1] = 1
        else:
            if 0 <= cur_position - 1 < 200000 and visited[cur_position - 1] == 0:
                stack.append((cur_position - 1, cur_time + 1))
                visited[cur_position - 1] == 1