N, M = map(int, input().split())
L = list(map(int, input().split()))
cand = []
sum = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            sum = L[i] + L[j] + L[k]
            if (sum <= M):
                cand.append(sum)
            sum = 0
                
print(max(cand))