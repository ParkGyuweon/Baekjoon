from collections import defaultdict, deque

def solution(N, roads, K):
    distance = [10E10] * (N + 1)
    graph = defaultdict(list)
    for road in roads:
        graph[road[0]].append((road[1], road[2]))
        graph[road[1]].append((road[0], road[2]))
    
    stack = deque([1])
    distance[1] = 0
    while stack:
        cur_vil = stack.popleft()
        for next_vil, weight in graph[cur_vil]:
            if distance[next_vil] > distance[cur_vil] + weight:
                stack.append(next_vil)
                distance[next_vil] = distance[cur_vil] + weight
                
    answer = 0
    for vil in distance:
        if vil != 10E10 and vil != 'INF' and vil <= K:
            answer += 1
    
    return answer