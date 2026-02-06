import sys
input = sys.stdin.readline
N = int(input().strip())
L = []
for i in range(N):
    L.append(list(map(int, input().strip().split())))
stage_sum = [] * N
stage_sum.append([L[0][0]])
index_list = [] * N
index_list.append([0])

def find_sum(N):
    for i in range(1, N):
        stage_part = dict()
        for j in range(len(index_list[i - 1])):
            index_num = index_list[i - 1][j]
            stage_num = stage_sum[i - 1][j]
            if (index_num + 1) in stage_part.keys():
                stage_part[index_num + 1] = max(stage_part[index_num + 1], stage_num + L[i][index_num + 1])
            else:
                stage_part[index_num + 1] = stage_num + L[i][index_num + 1]
            if (index_num) in stage_part.keys():
                stage_part[index_num] = max(stage_part[index_num], stage_num + L[i][index_num])
            else:
                stage_part[index_num] = stage_num + L[i][index_num]
        stage_sum.append(list(stage_part.values()))
        index_list.append(list(stage_part.keys()))

    return max(stage_sum[N - 1])

print(find_sum(N))