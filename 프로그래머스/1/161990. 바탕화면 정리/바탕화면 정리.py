def solution(wallpaper):
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    x_list, y_list = [], []
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[0])):
            if wallpaper[y][x] == '#':
                x_list.append(x)
                y_list.append(y)
    min_x = min(x_list)
    max_x = max(x_list) + 1
    min_y = min(y_list)
    max_y = max(y_list) + 1
    
    return [min_y, min_x, max_y, max_x]