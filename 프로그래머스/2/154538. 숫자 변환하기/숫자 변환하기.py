from collections import deque

def solution(x, y, n):
    if y < x:
        return - 1
    elif x == y:
        return 0
    else:
        queue = deque([(x, 0)])
        visited = [0] * 1000001
        visited[x] = 1
        while queue:
            cur_num, cur_turn = queue.popleft()
            if 0 <= cur_num + n <= 1000000 and visited[cur_num + n] == 0:
                if cur_num + n == y:
                    return cur_turn + 1
                visited[cur_num + n] = 1
                queue.append((cur_num + n, cur_turn + 1))
            if 0 <= cur_num * 2 <= 1000000 and visited[cur_num * 2] == 0:
                if cur_num * 2 == y:
                    return cur_turn + 1
                visited[cur_num * 2] = 1
                queue.append((cur_num * 2, cur_turn + 1))
            if 0 <= cur_num * 3 <= 1000000 and visited[cur_num * 3] == 0:
                if cur_num * 3 == y:
                    return cur_turn + 1
                visited[cur_num * 3] = 1
                queue.append((cur_num * 3, cur_turn + 1))
            
        return -1