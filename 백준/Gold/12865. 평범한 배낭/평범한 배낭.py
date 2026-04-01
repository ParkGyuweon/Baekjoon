import sys
input = sys.stdin.readline
N, K = map(int, input().split())
weight = [0] * (N + 1)
value = [0] * (N + 1)
for i in range(1, N + 1):
    weight[i], value[i] = map(int, input().split())

DP = [[0] * (K + 1) for _ in range(N + 1)]
for cur_object in range(1, N + 1):
    for limit in range(1, K + 1):
        if weight[cur_object] <= limit:
            DP[cur_object][limit] = max(DP[cur_object - 1][limit], DP[cur_object - 1][limit - weight[cur_object]] + value[cur_object])
        else:
            DP[cur_object][limit] = DP[cur_object - 1][limit]
print(DP[-1][-1])