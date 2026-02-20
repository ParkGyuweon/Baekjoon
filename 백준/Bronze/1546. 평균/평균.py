N = int(input())
L = list(map(int, input().split()))
sum = 0

max_number = max(L)

for i in range(len(L)):
    L[i] = (L[i] / max_number) * 100

for i in range(len(L)):
    sum = sum + L[i]
    
print(sum / len(L))