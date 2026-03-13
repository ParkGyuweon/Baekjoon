from collections import deque

N = int(input())
number = N
cnt = 0

def squares_bfs(N):
    stack = deque([(N, 0)])
    visited = [False] * 50000
    while stack:
        cur_number, cur_cnt = stack.popleft()
        for i in range(int(cur_number ** (1 / 2)), -1, -1):
            new_number = cur_number - i ** 2
            if new_number < 0:
                continue
            if new_number == 0:
                print(cur_cnt + 1)
                return
            if not visited[new_number - 1]:
                stack.append((new_number, cur_cnt + 1))
                visited[new_number - 1] = True

squares_bfs(N)