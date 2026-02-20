for t in range(1, 11):
    N, S = input().split()
    N = int(N)
    result, idx = [], 0

    for idx in range(len(S)):
        if result and result[-1] == S[idx]:
            result.pop()
        else:
            result.append(S[idx])

    print(f'#{t} {"".join(result)}')