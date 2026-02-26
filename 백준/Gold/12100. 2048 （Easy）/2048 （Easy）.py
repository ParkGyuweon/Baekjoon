from collections import deque

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
max_val = 0

for i in range(N):
    if max_val < max(grid[i]):
        max_val = max(grid[i])

def change_grid(grid, direction):
    global max_val
    if direction == 'D':
        for x in range(N):
            temp = deque()
            for idx in range(N):
                if grid[idx][x] != 0:
                    temp.append(grid[idx][x])
                elif grid[idx][x] == 0:
                    temp.appendleft(0)
            temp = list(temp)
            for y in range(N - 1, 0, -1):
                if temp[y] == 0:
                    break
                if temp[y] == temp[y - 1]:
                    temp[y] = temp[y] * 2
                    if temp[y] > max_val:
                        max_val = temp[y]
                    temp.pop(y - 1)
                    temp.insert(0, 0)

            for idx in range(N):
                grid[idx][x] = temp[idx]

    elif direction == 'U':
        for x in range(N):
            temp = deque()
            zero_cnt = 0
            for idx in range(N):
                if grid[idx][x] != 0:
                    temp.append(grid[idx][x])
                elif grid[idx][x] == 0:
                    zero_cnt += 1
            for i in range(zero_cnt):
                temp.append(0)
            temp = list(temp)
            for y in range(N - 1):
                if temp[y] == 0:
                    break
                if temp[y] == temp[y + 1]:
                    temp[y] = temp[y] * 2
                    if temp[y] > max_val:
                        max_val = temp[y]
                    temp.pop(y + 1)
                    temp.append(0)

            for idx in range(N):
                grid[idx][x] = temp[idx]

    elif direction == 'R':
        for y in range(N):
            temp = deque()
            for x in range(N):
                if grid[y][x] != 0:
                    temp.append(grid[y][x])
                else:
                    temp.appendleft(0)
            temp = list(temp)
            for x in range(N - 1, 0, -1):
                if temp[x] == 0:
                    break
                if temp[x] == temp[x - 1]:
                    temp[x] = temp[x] * 2
                    if temp[x] > max_val:
                        max_val = temp[x]
                    temp.pop(x - 1)
                    temp.insert(0, 0)

            grid[y] = temp

    elif direction == 'L':
        for y in range(N):
            zero_cnt = 0
            temp = deque()
            for x in range(N):
                if grid[y][x] != 0:
                    temp.append(grid[y][x])
                else:
                    zero_cnt += 1
            for i in range(zero_cnt):
                temp.append(0)
            temp = list(temp)
            for x in range(N - 1):
                if temp[x] == 0:
                    break
                if temp[x] == temp[x + 1]:
                    temp[x] = temp[x] * 2
                    if temp[x] > max_val:
                        max_val = temp[x]
                    temp.pop(x + 1)
                    temp.append(0)
            grid[y] = temp

def back(grid, cur_move):
    if cur_move >= 5:
        return
    for direction in ['D', 'U', 'R', 'L']:
        total_temp = [grid[y][:] for y in range(N)]
        change_grid(total_temp, direction)
        back(total_temp, cur_move + 1)

back(grid, 0)
print(max_val)