def dungeon_back(cur_health, visited, dungeons):
    global answer
    if sum(visited) == len(dungeons):
        return
    for idx in range(len(dungeons)):
        item = dungeons[idx]
        if visited[idx] == 0 and item[0] <= cur_health:
            visited[idx] = 1
            answer = max(answer, sum(visited))
            dungeon_back(cur_health - item[1], visited, dungeons)
            visited[idx] = 0
            
answer = 0
def solution(k, dungeons):
    global answer
    visited = [0] * len(dungeons)
    dungeon_back(k, visited, dungeons)
    return answer