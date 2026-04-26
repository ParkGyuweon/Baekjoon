from collections import deque

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    queue = deque([(N, 0)])
    visited = [0] * 1000001
    visited[N] = 1
    while queue:
        cur_number, cur_turn = queue.popleft()
        if 1 <= cur_number + 1 <= 1000000 and visited[cur_number + 1] == 0:
            if cur_number + 1 == M:
                print(f'#{t} {cur_turn + 1}')
                break
            visited[cur_number + 1] = 1
            queue.append((cur_number + 1, cur_turn + 1))
        if 1 <= cur_number - 1 <= 1000000 and visited[cur_number - 1] == 0:
            if cur_number - 1 == M:
                print(f'#{t} {cur_turn + 1}')
                break
            visited[cur_number - 1] = 1
            queue.append((cur_number - 1, cur_turn + 1))
        if 1 <= cur_number * 2 <= 1000000 and visited[cur_number * 2] == 0:
            if cur_number * 2 == M:
                print(f'#{t} {cur_turn + 1}')
                break
            visited[cur_number * 2] = 1
            queue.append((cur_number * 2, cur_turn + 1))
        if 1 <= cur_number - 10 <= 1000000 and visited[cur_number - 10] == 0:
            if cur_number - 10 == M:
                print(f'#{t} {cur_turn + 1}')
                break
            visited[cur_number - 10] = 1
            queue.append((cur_number - 10, cur_turn + 1))