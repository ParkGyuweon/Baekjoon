N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
white_num, blue_num = 0, 0

def paper(start_x, start_y, end_x, end_y):
    global white_num, blue_num
    if start_x == end_x and start_y == end_y:
        if grid[start_y][start_x] == 0:
            white_num += 1
        else:
            blue_num += 1
        return
    color = grid[start_y][start_x]
    for y in range(start_y, end_y + 1):
        if grid[y][start_x: end_x + 1] != [color] * (end_x - start_x + 1):
            break
    else:
        if color == 0:
            white_num += 1
        else:
            blue_num += 1
        return
    paper(start_x, start_y, (start_x + end_x) // 2, (start_y + end_y) // 2)
    paper((start_x + end_x) // 2 + 1, start_y, end_x, (start_y + end_y) // 2)
    paper(start_x, (start_y + end_y) // 2 + 1, (start_x + end_x) // 2, end_y)
    paper((start_x + end_x) // 2 + 1, (start_y + end_y) // 2 + 1, end_x, end_y)

paper(0, 0, N - 1, N - 1)
print(white_num)
print(blue_num)