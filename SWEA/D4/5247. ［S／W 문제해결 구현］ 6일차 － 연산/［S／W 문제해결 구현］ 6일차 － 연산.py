from collections import deque

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    stack = deque([(N, 0)])
    visited[N] = 1
    while stack:
        cur_number, cur_move = stack.popleft()
        if cur_number == M:
            print(f'#{t} {cur_move}')
            break
        if 1 <= cur_number - 1 <= 1000000 and visited[cur_number - 1] == 0:
            visited[cur_number - 1] = 1
            stack.append((cur_number - 1, cur_move + 1))
        if 1 <= cur_number - 10 <= 1000000 and visited[cur_number - 10] == 0:
            visited[cur_number - 10] = 1
            stack.append((cur_number - 10, cur_move + 1))
        if M >= N:
            if 1 <= cur_number + 1 <= 1000000 and visited[cur_number + 1] == 0:
                visited[cur_number + 1] = 1
                stack.append((cur_number + 1, cur_move + 1))
            if 1 <= cur_number * 2 <= 1000000 and visited[cur_number * 2] == 0:
                visited[cur_number * 2] = 1
                stack.append((cur_number * 2, cur_move + 1))

