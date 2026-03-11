from collections import deque
N = int(input())

def bfs():
    stack = deque([(N, 0)])
    while stack:
        cur_num, cur_cnt = stack.popleft()
        if cur_num % 3 == 0:
            new_num = cur_num // 3
            if new_num == 1:
                print(cur_cnt + 1)
                return
            stack.append((new_num, cur_cnt + 1))
        if cur_num % 2 == 0:
            new_num = cur_num // 2
            if new_num == 1:
                print(cur_cnt + 1)
                return
            stack.append((new_num, cur_cnt + 1))
        if cur_num - 1 == 1:
            print(cur_cnt + 1)
            return
        stack.append((cur_num - 1, cur_cnt + 1))
if N == 1:
    print(0)
else:
    bfs()