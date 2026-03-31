import sys
input = sys.stdin.readline
from collections import deque
R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]
visited = [0] * 26
visited[ord(grid[0][0]) - 65] = 1
stack = deque([[0, 0, visited]])
direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
max_move = 0

while stack:
    cur_x, cur_y, cur_visited = stack.pop()
    flag = False
    for x, y in direction:
        new_x, new_y = cur_x + x, cur_y + y
        if 0 <= new_x < C and 0 <= new_y < R and cur_visited[ord(grid[new_y][new_x]) - 65] == 0:
            flag = True
            new_visited = cur_visited[:]
            new_visited[ord(grid[new_y][new_x]) - 65] = new_visited[ord(grid[cur_y][cur_x]) - 65] + 1
            stack.append([new_x, new_y, new_visited])
    if not flag:
        max_move = max(max_move, cur_visited[ord(grid[cur_y][cur_x]) - 65])
        
print(max_move)