from collections import deque
import heapq
T = int(input())
direction = {'U': [(1, 0, 1, 'R'), (-1, 0, 1, 'L'), (0, -1, 0, 'U'), (0, 1, 2, 'D')],
             'R': [(1, 0, 0, 'R'), (-1, 0, 2, 'L'), (0, -1, 1, 'U'), (0, 1, 1, 'D')],
             'L': [(1, 0, 2, 'R'), (-1, 0, 0, 'L'), (0, -1, 1, 'U'), (0, 1, 1, 'D')],
             'D': [(1, 0, 1, 'R'), (-1, 0, 1, 'L'), (0, -1, 2, 'U'), (0, 1, 0, 'D')]}

for t in range(1, T + 1):
    N, K = map(int, input().split())
    grid = [list(input()) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 'X':
                start_x, start_y = x, y
            elif grid[y][x] == 'Y':
                end_x, end_y = x, y

    def cut_tree(start_x, start_y, end_x, end_y):
        stack = [(0, start_x, start_y, 0, 'U')]
        visited = [[[0 for _ in range(K + 1)] for _ in range(N)] for _ in range(N)]
        while stack:
            cur_move, cur_x, cur_y, cur_tree, cur_direction = heapq.heappop(stack)
            if cur_x == end_x and cur_y == end_y:
                return cur_move
            for x, y, add_move, next_direction in direction[cur_direction]:
                new_x, new_y = cur_x + x, cur_y + y
                if 0 <= new_x < N and 0 <= new_y < N:
                    if (grid[new_y][new_x] == 'G' or grid[new_y][new_x] == 'Y') and visited[new_y][new_x][cur_tree] == 0:
                        visited[new_y][new_x][cur_tree] = 1
                        heapq.heappush(stack, (cur_move + 1 + add_move, new_x, new_y, cur_tree, next_direction))
                    elif grid[new_y][new_x] == 'T' and cur_tree + 1 <= K and visited[new_y][new_x][cur_tree + 1] == 0:
                        visited[new_y][new_x][cur_tree + 1] = 1
                        heapq.heappush(stack, (cur_move + 1 + add_move, new_x, new_y, cur_tree + 1, next_direction))

    result = cut_tree(start_x, start_y, end_x, end_y)
    if result == None:
        print(f'#{t} -1')
    else:
        print(f'#{t} {result}')