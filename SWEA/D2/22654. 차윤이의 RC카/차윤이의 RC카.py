from collections import deque
import heapq
T = int(input())
direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]

for t in range(1, T + 1):
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    answer = []
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 'X':
                start_x, start_y = x, y
            elif grid[y][x] == 'Y':
                end_x, end_y = x, y

    Q = int(input())
    for number in range(Q):
        _, command = input().split()
        cur_x, cur_y, cur_direction = start_x, start_y, 0
        for character in command:
            if character == 'R':
                cur_x, cur_y, cur_direction = cur_x, cur_y, (cur_direction + 1) % 4
            elif character == 'L':
                cur_x, cur_y, cur_direction = cur_x, cur_y, (cur_direction + 3) % 4
            else:
                new_x, new_y, cur_direction = cur_x + direction[cur_direction][0], cur_y + direction[cur_direction][1], cur_direction
                if 0 <= new_x < N and 0 <= new_y < N and (grid[new_y][new_x] != 'T'):
                    cur_x, cur_y = new_x, new_y

        if cur_x == end_x and cur_y == end_y:
            answer.append(1)
        else:
            answer.append(0)

    print(f'#{t} {" ".join(map(str, answer))}')