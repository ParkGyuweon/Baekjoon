T = int(input())

for i in range(T):
    answer = 'yes'
    S = input().strip()
    set_string = list(set(S))
    while set_string:
        number = set_string[-1]
        if S.count(number) != 0 and S.count(number) != 2:
            answer = 'no'
            break
        elif S.count(number) == 2:
            idx = S.index(number)
            if len(S) <= idx + int(number) + 1:
                answer = 'no'
                break
            if S[idx + int(number) + 1] == number:
                answer = 'yes'
                set_string.pop()
            else:
                answer = 'no'
                break
    print(answer)
                
           	
        
        