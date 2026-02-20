N = int(input())
L = []
for i in range(N):
    S = input()
    L.append([len(S), S])
    
L.sort(key = lambda x: [x[0], x[1]])

print(L[0][1])
for i in range(1, N):
    if (L[i][1] != L[i - 1][1]):
        print(L[i][1])