from collections import deque

N = int(input())

D = deque(range(1, N + 1))
while len(D)!= 1:
    M = D.popleft()
    D.rotate(-1)
    
print(D[0])