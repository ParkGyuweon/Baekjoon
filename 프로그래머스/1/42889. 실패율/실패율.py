def solution(N, stages):
    count_stage = [0] * (N + 2)
    
    fail_rate = [[i + 1, 0] for i in range(N)]
    for stage in stages:
        count_stage[stage] += 1
    for idx in range(len(count_stage) - 1, 0, -1):
        count_stage[idx - 1] += count_stage[idx]
    
    for idx in range(1, N + 1):
        if count_stage[idx] == 0:
            fail_rate[idx - 1][1] = 0
        else:
            fail_rate[idx - 1][1] = 1 - (count_stage[idx + 1]) / count_stage[idx]
        
    total_list = list(sorted(fail_rate, key=lambda x:(-x[1], x[0])))
    answer = []
    for each in total_list:
        answer.append(each[0])
    
    return answer