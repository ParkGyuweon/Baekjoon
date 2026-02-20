T = int(input())

for t in range(1, T + 1):
    case = [list(reversed(input())) for _ in range(5)]
    result, idx, max_val = [], 0, max(len(case[0]), len(case[1]), len(case[2]), len(case[3]), len(case[4]))

    for idx in range(max_val):
        for i in range(len(case)):
            if case[i]:
                result.append(case[i].pop())

    print(f'#{t} {"".join(result)}')
