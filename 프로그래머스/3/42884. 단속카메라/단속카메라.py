def solution(routes):
    routes.sort(key=lambda x:x[1])
    
    cur_end = routes[0][1]
    answer = 1
    
    for route in routes:
        if route[0] <= cur_end:
            continue
        else:
            answer += 1
            cur_end = route[1]
    print(routes)
    return answer