N = int(input())
L = list(map(int, input().split()))
k = 0

for j in range(len(L)):
    i = 0
    num = 1
    while num <= (L[j]**(1/2)):
        if (L[j] % num == 0):
            i = i + 1
        num = num + 1
    if (i == 1):
        k = k + 1
    if (L[j] == 1):
        k = k - 1
        
print(k)