N = int(input())
L = [] 
for i in range(N):
    L.append(list(map(int, input().split())))
stage_amount = [[0] * 3 for _ in range(N)]
stage_amount[0][0] = L[0][0]
stage_amount[0][1] = L[0][1]
stage_amount[0][2] = L[0][2]
def color(N):
    for i in range(1, N):
        stage_amount[i][0] = L[i][0] + min(stage_amount[i - 1][1], stage_amount[i - 1][2])
        stage_amount[i][1] = L[i][1] + min(stage_amount[i - 1][0], stage_amount[i - 1][2])
        stage_amount[i][2] = L[i][2] + min(stage_amount[i - 1][0], stage_amount[i - 1][1])
    return min(stage_amount[N - 1])

print(color(N))