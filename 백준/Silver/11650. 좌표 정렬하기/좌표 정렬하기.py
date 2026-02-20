N = int(input())
L = []

for i in range(N):
    num = list(map(int, input().split()))
    L.append(num)
    
L.sort(key=lambda x: [x[0], x[1]])

for i in range(N):
    print(L[i][0], L[i][1])  