N = int(input())
stair_list = [0] * N
stair_list[0:3] = [0, 1, 1]

for stair in range(3, N):
    stair_list[stair] = stair_list[stair - 2] + stair_list[stair - 3]

if stair_list[N - 1] != 0:
    print(stair_list[N - 1] % 10007)
else:
    print(0)