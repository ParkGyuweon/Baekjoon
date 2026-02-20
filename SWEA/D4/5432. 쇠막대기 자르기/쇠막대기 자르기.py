T = int(input())
 
for t in range(1, T + 1):
    S = input()
    S_list = list(S.replace('()', ' '))
    idx, cnt, result = 0, 0, []
 
    while idx != len(S_list):
        if S_list[idx] == '(':
            result.append(S_list[idx])
        elif S_list[idx] == ' ':
            cnt = cnt + len(result)
        elif S_list[idx] == ')':
            result.pop()
        idx = idx + 1
 
    print(f'#{t} {cnt + S_list.count("(")}')