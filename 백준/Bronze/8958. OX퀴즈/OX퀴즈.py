T = int(input())
for t in range(1, T + 1):
    one_line = list(input() + 'X')
    sum_val, cnt = 0, 0
    for i in range(len(one_line)):
        if one_line[i] == 'O':
            cnt += 1
        elif one_line[i] == 'X':
            cnt = 0
        sum_val = sum_val + cnt
    print(sum_val)