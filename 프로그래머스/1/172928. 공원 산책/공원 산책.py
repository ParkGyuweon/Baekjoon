def solution(park, routes):
    for y in range(len(park)):
        for x in range(len(park[0])):
            if park[y][x] == 'S':
                cur_x, cur_y = x, y
                
    dir = {'E' : (1, 0), 'N' : (0, -1), 'S' : (0, 1), 'W' : (-1, 0)}         
    for route in routes:
        direction, distance = route.split()
        next_x, next_y = cur_x, cur_y
        for move in range(int(distance)):
            new_y = next_y + dir[direction][1]
            new_x = next_x + dir[direction][0]
            if 0 <= new_x < len(park[0]) and 0 <= new_y < len(park) and park[new_y][new_x] != 'X':
                next_x, next_y = new_x, new_y
            else:
                break
        else:
            cur_x, cur_y = next_x, next_y
    return [cur_y, cur_x]