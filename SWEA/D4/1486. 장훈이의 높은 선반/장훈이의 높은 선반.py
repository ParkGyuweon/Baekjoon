T = int(input())

def back(sum, B, start, diff):
    global min_value
    if start + diff >= N:
        return
    sum = sum + L[start + diff]       
    if sum - B >= min_value:
        return
    if sum >= B and sum - B < min_value:
        min_value = sum - B
    for j in range(1, N):
        back(sum, B, start, diff + j)
        
for k in range(T):
    N, B = map(int, input().split())
    L = list(map(int, input().split()))
    min_value = 10E10
    for i in range(N):
        sum = 0
        start = i
        back(sum, B, start, 0)
    print(f'#{k + 1} {min_value}')