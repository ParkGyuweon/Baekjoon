from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    
    for item in cities:
        if item.upper() not in cache:
            answer += 5
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(item.upper())
        else:
            cache.remove(item.upper())
            cache.append(item.upper())
            answer += 1        
    return answer