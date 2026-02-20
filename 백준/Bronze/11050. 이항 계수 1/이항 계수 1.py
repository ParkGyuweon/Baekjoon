N, K = map(int, input().split())
sum1= 1
sum2 = 1
sum3 = 1
for i in range(1, N + 1):
    sum1 = sum1 * i

for i in range(1, K + 1):
    sum2 = sum2 * i
    
for i in range(1, N - K + 1):
    sum3 = sum3 * i
    
print(sum1 // (sum2 * sum3))