from collections import deque
for t in range(1, 11):
    N = int(input())
    
    if N == 1:
        print(f'#{t} 64')
    else:
        grid = [list(input()) for _ in range(8)]
        cnt = 0
        for y in range(8):
            for x in range(8 - N + 1):
                one_line = deque(grid[y][x:x + N])
                while one_line.popleft() == one_line.pop():
                    if len(one_line) <= 1:
                        cnt = cnt + 1
                        break

        grid = list(zip(*grid))
        for y in range(8):
            for x in range(8 - N + 1):
                one_line = deque(grid[y][x : x + N])
                while one_line.popleft() == one_line.pop():
                    if len(one_line) <= 1:
                        cnt = cnt + 1
                        break

        print(f'#{t} {cnt}')