import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().strip().split())

L = [[0] * (M + 2)]
for i in range(N):
    L.append('0' + input().strip() + '0')
L.append([0] * (M + 2))

def possible(y, x):
    if x >= 1 and x <= M:
        if y >= 1 and y <= N:
            if int(L[y][x]) == 1 and not visited[y][x]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

visited = [[False] * (M + 2) for _ in range(N + 2)]
candidate = deque()
def mirror():
    candidate.append([1, 1, 1])
    visited[1][1] = True
    while candidate:
        listing = candidate.popleft()
        y = listing[0]
        x = listing[1]
        count = listing[2]
        if y == N and x == M:
            print(count)
            return
        if possible(y, x + 1):
            visited[y][x + 1] = True
            candidate.append([y, x + 1, count + 1])
        if possible(y, x - 1):
            visited[y][x - 1] = True
            candidate.append([y, x - 1, count + 1])
        if possible(y + 1, x):
            visited[y + 1][x] = True
            visited[y + 1][x] = True
            candidate.append([y + 1, x, count + 1])
        if possible(y - 1, x):
            visited[y - 1][x] = True
            visited[y - 1][x] = True
            candidate.append([y - 1, x, count + 1])

mirror()