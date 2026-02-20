import sys
input = sys.stdin.readline
from collections import defaultdict
T = int(input())

for t in range(1, T + 1):
    floor_dir = defaultdict(list)
    total = 0
    k = int(input().strip())
    n = int(input().strip())
    floor = list(range(1, n + 1))
    for i in range(k):
        for j in range(n - 1, -1, -1):
            floor[j] = sum(floor[:j + 1])
    print(floor[n - 1])