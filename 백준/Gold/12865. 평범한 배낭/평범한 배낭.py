import sys
input = sys.stdin.readline
N, K = map(int, input().split())
weight = [0] * (N + 1)
value = [0] * (N + 1)
DP = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    weight[i], value[i] = map(int, input().split())

for cur_object in range(1, N + 1):
    for cur_weight in range(K + 1):
        if weight[cur_object] <= cur_weight:
            DP[cur_object][cur_weight] = max(DP[cur_object - 1][cur_weight], DP[cur_object - 1][cur_weight - weight[cur_object]] + value[cur_object])
        else:
            DP[cur_object][cur_weight] = DP[cur_object - 1][cur_weight]

print(DP[-1][-1])

