occation = int(input())
L = []
for i in range(occation):
    L.append(list(map(int, input().split())))
   
for i in range(occation):
    sum1 = 1
    sum2 = 1
    sum3 = 1
    for j in range(1, L[i][1] + 1):
        sum1 = sum1 * j
    for j in range(1, L[i][0] + 1):
        sum2 = sum2 * j
    for j in range(1, L[i][1] - L[i][0] + 1):
        sum3 = sum3 * j
    print(sum1 // (sum2 * sum3))