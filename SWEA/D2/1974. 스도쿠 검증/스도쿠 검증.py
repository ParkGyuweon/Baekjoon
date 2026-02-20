T = int(input())

for t in range(1, T + 1):
    grid = [list(map(int, input().split())) for _ in range(9)]

    flag = True
    for row in range(9):
        if len(set(grid[row])) != 9:
            flag = False
    for col in range(9):
        if len(set(list(zip(*grid))[col])) != 9:
            flag = False

    row, col = 1, 1
    for i in range(9):
        one_kan = set()
        for check_x, check_y in [(1, 1), (1, 0), (1, -1), (0, 1), (0, 0), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
            one_kan.add(grid[row + check_y][col + check_x])
        if len(one_kan) != 9:
            flag = False
        row = row + 3
        if row > 9:
            row = row % 9
            col = col + 3

    if flag:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')