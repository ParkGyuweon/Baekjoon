T = int(input())

for t in range(1, T + 1):
    check = list(input())
    result, flag, opening, closing = [], True, ['(', '{'], [')', '}']

    for i in range(len(check)):
        if check[i] in opening:
            result.append(check[i])
        elif check[i] in closing:
            if not result:
                flag = False
                break
            if opening.index(result.pop()) != closing.index(check[i]):
                flag = False
                break

    if result:
        flag = False
    if flag:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
