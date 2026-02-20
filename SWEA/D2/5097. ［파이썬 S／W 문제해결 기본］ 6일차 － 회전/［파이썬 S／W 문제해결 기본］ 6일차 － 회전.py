from collections import deque

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    number = deque(map(int, input().split()))
    number.rotate(-M)
    print(f'#{t} {number[0]}')