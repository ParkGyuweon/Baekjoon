from collections import defaultdict
import sys
input = sys.stdin.readline
T = int(input().strip())

for t in range(1, T + 1):

    clothes_dict = defaultdict(int)
    N = int(input())
    for i in range(N):
        item, kind = input().split()
        clothes_dict[kind] += 1

    solution = 1
    for key, value in clothes_dict.items():
        solution = solution * (value + 1)

    print(solution - 1)