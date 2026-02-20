from collections import deque

N, K = map(int, input().split())
L = []

D = deque(range(1, N + 1))
while len(D) != 0:
    D.rotate(-K + 1)
    L.append(D.popleft())
    
print('<' + ', '.join(map(str, L)) + '>')