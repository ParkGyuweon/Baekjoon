from collections import deque

T = int(input())

for i in range(T):
    S = deque(input().strip())
    N = int(input())
    K = list(map(int, input().split()))
    
    for number in K:
        if number > 0:
            S.rotate(-1 * number)
        elif number < 0:
            S.rotate(-1 * number)
        else:
            continue
    print(''.join(list(S)))