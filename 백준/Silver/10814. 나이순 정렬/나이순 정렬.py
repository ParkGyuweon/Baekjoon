N = int(input())
L = []
t = 0

for i in range(N):
    num, S = map(str, input().split())
    L.append([int(num), S, t])
    t = t + 1
    
L.sort(key = lambda x: [x[0], x[2]])

for i in range(N):
    print(L[i][0], L[i][1])