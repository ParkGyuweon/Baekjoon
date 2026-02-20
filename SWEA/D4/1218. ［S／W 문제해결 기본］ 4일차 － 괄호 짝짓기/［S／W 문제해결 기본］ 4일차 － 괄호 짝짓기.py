for t in range(1, 11):
    N = int(input())
    S = list(input())
    result, flag, opening, closing = [], True, ['(', '[', '{', '<'], [')', ']', '}', '>']
    
    for idx in range(len(S)):
        if S[idx] in opening:
            result.append(S[idx])
        elif S[idx] in closing and (opening.index(result[-1]) == closing.index(S[idx])):
                result.pop()
        else:
            flag = False
            break
 
    if flag:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')