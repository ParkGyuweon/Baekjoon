import heapq

def solution(jobs):
    waiting = []
    disk_busy = False
    time_table = [[] for _ in range(1001)]
    answer = []
    
    for idx in range(len(jobs)):
        time_table[jobs[idx][0]].append((jobs[idx][1], jobs[idx][0], idx))
    
    t = 0
    while len(answer) < len(jobs):
        if disk_busy and t >= end_time:
            disk_busy = False
            
        if t <= 1000:
            for job in time_table[t]:
                heapq.heappush(waiting, job)
        
        if not disk_busy and waiting:
            cur_worktime, cur_time, cur_work = heapq.heappop(waiting)
            disk_busy = True
            end_time = t + cur_worktime
            answer.append(end_time - cur_time)
        t += 1
        
    return sum(answer) // len(answer)