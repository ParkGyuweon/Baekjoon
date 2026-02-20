T = int(input())
for i in range(T):
    L = list(map(int, input().split()))
    sum = 0
    for j in range(10):
        if L[j] % 2 != 0:
            sum = sum  + L[j]
                
    print(f'#{i + 1} {sum}')