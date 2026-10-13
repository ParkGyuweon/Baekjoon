from collections import deque

def check(x, y, maps):
    if 0 <= x < len(maps[0]) and 0 <= y < len(maps):
        return True
    return False

def solution(maps):
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == 'S':
                start_x, start_y = x, y
            elif maps[y][x] == 'L':
                lever_x, lever_y = x, y
            elif maps[y][x] == 'E':
                end_x, end_y = x, y
    
    time = 0
    stack = deque([(start_x, start_y)])
    
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[start_y][start_x] = 0
    stop = 0
    while stack:
        cur_x, cur_y = stack.popleft()
        for x, y in direction:
            if check(cur_x + x, cur_y + y, maps) and maps[cur_y + y][cur_x+x] != 'X' and visited[cur_y + y][cur_x + x] == -1:
                if cur_x + x == lever_x and cur_y + y == lever_y:
                    time += visited[cur_y][cur_x] + 1
                    stop = 1
                    break
                stack.append((cur_x + x, cur_y + y))
                visited[cur_y + y][cur_x + x] = visited[cur_y][cur_x] + 1
        if stop == 1:
            break
    else:
        return -1
    
    stack = deque([(lever_x, lever_y)])
    visited = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visited[lever_y][lever_x] = 0
    stop = 0
    while stack:
        cur_x, cur_y = stack.popleft()
        for x, y in direction:
            if check(cur_x + x, cur_y + y, maps) and maps[cur_y + y][cur_x+x] != 'X' and visited[cur_y + y][cur_x + x] == -1:
                if cur_x + x == end_x and cur_y + y == end_y:
                    time += visited[cur_y][cur_x] + 1
                    stop = 1
                    break
                stack.append((cur_x + x, cur_y + y))
                visited[cur_y + y][cur_x + x] = visited[cur_y][cur_x] + 1
        if stop == 1:
            break
    else:
        return -1
    
    return time