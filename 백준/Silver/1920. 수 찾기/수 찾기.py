N = int(input())
S_N = set(map(int, input().split()))
M = int(input())
for i in list(map(int, input().split())):
    if i in S_N:
        print(1)
    else:
        print(0)