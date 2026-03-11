import sys
input = sys.stdin.readline

N, M = map(int, input().split())
site_dict = {}
for i in range(N):
    command = input().strip().split()
    site_dict[command[0]] = command[1]
for j in range(M):
    site = input().strip()
    print(site_dict[site])