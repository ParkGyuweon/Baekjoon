from heapq import heappop, heappush, heapify

def solution(scoville, K):
    heapify(scoville) 
    turn = 0
    while scoville[0] < K and len(scoville) >= 2:
        food_min = heappop(scoville)
        food_max = heappop(scoville)
        heappush(scoville, food_min + food_max * 2)
        turn += 1
    if scoville and min(scoville) >= K:
        return turn
    else:
        return -1