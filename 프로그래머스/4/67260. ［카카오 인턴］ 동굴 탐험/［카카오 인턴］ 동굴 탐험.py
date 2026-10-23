from collections import deque, defaultdict

def solution(n, path, order):
    stack = deque([0])
    needs = [0] * n
    
    for before, after in order:
        needs[after] = before
        # after를 가려면 before를 먼저 방문해야 함
        if after == 0 and before != 0:
            return False
        
    visited = [0] * n
    visited[0] = 1
    
    paths = defaultdict(list)
    for before, after in path:
        paths[before].append(after)
        paths[after].append(before)
    
    waiting = [0] * n
    while stack:
        cur_place = stack.popleft()
        for room in paths[cur_place]:
            if visited[room] == 0 and (needs[room] == 0 or visited[needs[room]] == 1):
                stack.append(room)
                visited[room] = 1
                
                if waiting[room] != 0:
                    # 이 방을 방문하면 뚫리는 장소가 있음
                    stack.appendleft(waiting[room]) 
                    visited[waiting[room]] = 1
                    # stack에 바로 해당 장소를 넣음
                    waiting[room] = 0
                    # 이 방은 이제 의미가 없어짐
                    
            elif visited[needs[room]] == 0: 
                waiting[needs[room]] = room
                # 방문해야 하는 방이 있는데 아직 방문하지 못한 경우
                # 해당 방을 방문하면, 원래 가려고 했던 방을 바로 stack에 넣으려고 함
    
    if sum(visited) == n:
        return True
    return False
            