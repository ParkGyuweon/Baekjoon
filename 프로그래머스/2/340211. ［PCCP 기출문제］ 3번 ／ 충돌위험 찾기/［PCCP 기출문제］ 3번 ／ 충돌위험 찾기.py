from collections import defaultdict

def solution(points, routes):
    time_table = defaultdict(list)
    for robot in routes:
        cur_r, cur_c = points[robot[0] - 1][0], points[robot[0] - 1][1]
        cur_num, next_num, cur_time = 0, 1, 1
        cur_place = robot[0]
        time_table[0].append((cur_r, cur_c))
        
        while cur_num < len(robot) - 1:
            cur_place = robot[cur_num]
            next_place = robot[next_num]
            while points[next_place - 1][0] < cur_r:
                time_table[cur_time].append((cur_r - 1, cur_c))
                cur_r -= 1
                cur_time += 1
            while points[next_place - 1][0] > cur_r:
                time_table[cur_time].append((cur_r + 1, cur_c))
                cur_r += 1
                cur_time += 1
            while points[next_place - 1][1] < cur_c:
                time_table[cur_time].append((cur_r, cur_c - 1))
                cur_c -= 1
                cur_time += 1
            while points[next_place - 1][1] > cur_c:
                time_table[cur_time].append((cur_r, cur_c + 1))
                cur_c += 1
                cur_time += 1
            cur_num += 1
            if len(robot) >= 2:
                next_num += 1
    answer = 0
    for key, item in time_table.items():
        visited = set()
        crush = set()
        for place in item:
            if place in visited:
                crush.add(place)
            visited.add(place)
        answer += len(crush)
    return answer