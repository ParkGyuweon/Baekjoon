def solution(dirs):
    road_set = set()
    direction = {'U' : (0, -1), 'D' : (0, 1), 'L' : (-1, 0), 'R' : (1, 0)}
    cur_x, cur_y = 0, 0
    for dir in dirs:
        new_x, new_y = cur_x + direction[dir][0], cur_y + direction[dir][1]
        if -5 <= new_x <= 5 and -5 <= new_y <= 5:
            road_set.add((cur_x, cur_y, new_x, new_y))
            road_set.add((new_x, new_y, cur_x, cur_y))
            cur_x, cur_y = new_x, new_y
    return len(road_set) // 2