from collections import defaultdict 

def solution(k, tangerine):
    answer = 0
    graph = defaultdict(int)
    for item in tangerine:
        graph[item] += 1
    
    key_list = sorted(graph.items(), key = lambda x:x[1])
    cur_fruit = 0
    while cur_fruit < k:
        cur_kind, cur_weight = key_list.pop()
        cur_fruit += cur_weight
        answer += 1
    return answer