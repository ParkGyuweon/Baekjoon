from collections import deque

A, B = map(int, input().split())
stack = deque([(A, 0)])
while stack:
    cur_num, cur_time = stack.popleft()
    if cur_num * 2 == B or cur_num * 10 + 1 == B:
        print(cur_time + 2)
        break
    if cur_num <= B:
        stack.append((cur_num * 2, cur_time + 1))
    if len(str(cur_num)) < len(str(B)):
        stack.append((cur_num * 10 + 1, cur_time + 1))
else:
    print(-1)