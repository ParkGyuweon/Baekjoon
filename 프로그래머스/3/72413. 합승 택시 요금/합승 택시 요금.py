from collections import deque, defaultdict

def solution(n, s, a, b, fares):
    total_distance = [[10E10 for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if x == y:
                total_distance[y][x] = 0
    p_to_p = defaultdict(list)
    for fare in fares:
        p_to_p[fare[0] - 1].append((fare[1] - 1, fare[2]))
        p_to_p[fare[1] - 1].append((fare[0] - 1, fare[2]))

    stack = deque([(s - 1, 0)])
    while stack:
        cur_place, cur_weight = stack.popleft()
        if cur_weight > total_distance[s - 1][cur_place]:
            continue
        for next_place, weight in p_to_p[cur_place]:
            if total_distance[s - 1][next_place] > cur_weight + weight:
                total_distance[s - 1][next_place] = cur_weight + weight
                total_distance[next_place][s - 1] = cur_weight + weight
                stack.append((next_place, cur_weight + weight))
    
    stack = deque([(a - 1, 0)])
    while stack:
        cur_place, cur_weight = stack.popleft()
        if cur_weight > total_distance[a - 1][cur_place]:
            continue
        for next_place, weight in p_to_p[cur_place]:
            if total_distance[a - 1][next_place] > cur_weight + weight:
                total_distance[a - 1][next_place] = cur_weight + weight
                total_distance[next_place][a - 1] = cur_weight + weight
                stack.append((next_place, cur_weight + weight))
                
    stack = deque([(b - 1, 0)])
    while stack:
        cur_place, cur_weight = stack.popleft()
        if cur_weight > total_distance[b - 1][cur_place]:
            continue
        for next_place, weight in p_to_p[cur_place]:
            if total_distance[b - 1][next_place] > cur_weight + weight:
                total_distance[b - 1][next_place] = cur_weight + weight
                total_distance[next_place][b - 1] = cur_weight + weight
                stack.append((next_place, cur_weight + weight))
    
    min_fee = 10E10
    for node in range(n):
        cur_fee = 0
        cur_fee += total_distance[s - 1][node]
        cur_fee += total_distance[node][a - 1]
        cur_fee += total_distance[node][b - 1]
        min_fee = min(min_fee, cur_fee)
        
    return min_fee