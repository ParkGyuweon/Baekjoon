from heapq import heappop, heappush

def solution(n, works):
    work_queue = []
    for item in works:
        heappush(work_queue, -1 * item)
    for _ in range(n):
        if work_queue:
            cur_work = heappop(work_queue)
            if cur_work != 0:
                heappush(work_queue, cur_work + 1)
    answer = 0
    for item in work_queue:
        answer += item ** 2
    return answer