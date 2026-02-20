T = int(input())

for t in range(1, T + 1):
    S = list(input())
    result = []
    idx = 0
    while idx != len(S):
        if result and result[-1] == S[idx]:
            result.pop()
            idx = idx + 1
        else:
            result.append(S[idx])
            idx = idx + 1

    print(f'#{t} {len(result)}')
