import heapq

def solution(picks, minerals):
    five_minerals = []
    for idx in range(0, sum(picks) * 5, 5):
        cur_part = minerals[idx:idx + 5]
        heapq.heappush(five_minerals, (-1 * cur_part.count('diamond'), -1 * cur_part.count('iron'), -1 * cur_part.count('stone')))
    
    answer = 0
    while five_minerals:
        cur_diamond, cur_iron, cur_stone = heapq.heappop(five_minerals)
        if picks[0] > 0:
            answer += -1 * (cur_diamond + cur_iron + cur_stone)
            picks[0] -= 1
        elif picks[1] > 0:
            answer += -1 * (cur_diamond * 5 + cur_iron + cur_stone)
            picks[1] -= 1
        elif picks[2] > 0:
            answer += -1 * (cur_diamond * 25 + cur_iron * 5 + cur_stone)
            picks[2] -= 1
    
    return answer