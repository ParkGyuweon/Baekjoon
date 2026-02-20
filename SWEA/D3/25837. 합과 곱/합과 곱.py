T = int(input())

for i in range(T):
    S, P = map(int, input().split())
    p_result = False
    if S >= 2:
        s_result = True
    else:
        s_result = False
    if s_result:
        for j in range(1, int(P ** (1/2)) + 1):
            if j * (S - j) == P:
                p_result = True
        if s_result and p_result:
            answer = 'Yes'
        else:
            answer = 'No'
    print(answer)