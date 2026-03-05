from collections import deque
T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    char_2 = deque()
    while M != 0:
        char_2.appendleft(M % 2)
        M = M // 2
    for i in range(N):
        if len(char_2) - 1 - i < 0 or len(char_2) - 1 - i >= len(char_2):
            print(f'#{t} OFF')
            break
        elif char_2[len(char_2) - 1 - i] != 1:
            print(f'#{t} OFF')
            break
    else:
        print(f'#{t} ON')
