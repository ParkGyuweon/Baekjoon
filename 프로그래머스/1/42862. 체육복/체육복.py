def solution(n, lost, reserve):
    
    common_student = set(reserve) & set(lost)
    reserve = sorted(list(set(reserve) - common_student))
    lost = sorted(list(set(lost) - common_student))
    
    answer = n - len(lost)
    
    reserve_point = 0
    while reserve_point < len(reserve):
        if reserve[reserve_point] - 1 in set(lost):
            lost.remove(reserve[reserve_point] - 1)
            reserve.pop(reserve_point)
            answer += 1
        elif reserve[reserve_point] + 1 in set(lost):
            lost.remove(reserve[reserve_point] + 1)
            reserve.pop(reserve_point)
            answer += 1
        else:
            reserve_point += 1
            
    return answer