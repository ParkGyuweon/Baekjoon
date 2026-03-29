import sys
input = sys.stdin.readline

T = int(input().strip())
for t in range(1, T + 1):
    a, b = map(int, input().split())
    answer = 1
    for i in range(b):
        answer = (a * answer) % 10
        
    if answer == 0:
        print(10)
    else:
        print(answer)