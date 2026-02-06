import sys

L_y = []
L_3 = []
place = []
for i in range(9):
    L_y.append(list(map(int, input().split())))
    for j in range(9):
        if L_y[i][j] == 0:
            place.append((i, j))
L_x = [list(row) for row in zip(*L_y)]

for i in range(0, 9, 3):
    L_3.append(L_y[i][0:3] + L_y[i + 1][0:3] + L_y[i + 2][0:3]) 
    L_3.append(L_y[i][3:6] + L_y[i + 1][3:6] + L_y[i + 2][3:6])
    L_3.append(L_y[i][6:9] + L_y[i + 1][6:9] + L_y[i + 2][6:9])
    
def possible(num, x, y):
    if num in L_y[y] or num in L_x[x]:
        return False
    elif num in L_3[x // 3 + (y // 3 * 3)]:
        return False
    else:
        return True
    
def back(count):
    if count == len(place):
        for i in range(9):
            print(' '.join(map(str, L_y[i])))
        sys.exit(0)
    else:
        y, x = place[count]
        for num in range(1, 10):
            if possible(num, x, y):
                L_y[y][x] = num
                L_x[x][y] = num
                L_3[x // 3 + (y // 3 * 3)][(y % 3 * 3 + x % 3)] = num
                
                back(count + 1)
                
                L_y[y][x] = 0
                L_x[x][y] = 0
                L_3[x // 3 + (y // 3 * 3)][(y % 3 * 3 + x % 3)] = 0
    return

back(0)  