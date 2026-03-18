N = int(input())
M = int(input())
S = input()

cur_length = 1 + 2 * N
result, idx, flag = 0, 0, False
cnt_list = [0] * M
while idx < M:
    if S[idx] == 'I' and not flag:
        cnt_list[idx] = 1
        if idx < M - 1 and S[idx] != S[idx + 1]:
            flag = True
    elif flag and S[idx - 1] != S[idx]:
        cnt_list[idx] = cnt_list[idx - 1] + 1
    elif flag and S[idx - 1] == S[idx]:
        flag = False
        if cnt_list[idx - 1] % 2 == 0:
            cnt_list[idx - 1] -= 1
        if cnt_list[idx - 1] >= cur_length:
            result += (cnt_list[idx - 1] - cur_length + 1) // 2 + 1
        idx -= 1
    idx += 1

if cnt_list[M - 1] % 2 == 0:
    cnt_list[M - 1] -= 1
if cnt_list[M - 1] >= cur_length:
    result += (cnt_list[M - 1] - cur_length + 1) // 2 + 1
print(result)