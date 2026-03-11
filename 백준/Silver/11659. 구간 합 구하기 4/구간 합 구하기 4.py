import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
number_list = list(map(int, input().split()))
for i in range(1, N):
    number_list[i] = number_list[i] + number_list[i - 1]

for i in range(M):
    start, end = map(int, input().split())
    if start == 1:
        print(str(number_list[end - 1]) + '\n')
    else:
        print(str(number_list[end - 1] - number_list[start - 2]) + '\n')