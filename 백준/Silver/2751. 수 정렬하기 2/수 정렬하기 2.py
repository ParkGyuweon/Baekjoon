import sys

N = int(sys.stdin.readline())
L = []
for i in range(N):
    M = int(sys.stdin.readline())
    L.append(M)

L.sort()

for i in range(N):
    print(L[i])