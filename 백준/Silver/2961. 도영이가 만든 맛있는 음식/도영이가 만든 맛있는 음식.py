N = int(input())
dishes = [tuple(map(int, input().split())) for _ in range(N)]
min_val = 10E10

for i in range(1, 1 << N):
    taste1, taste2 = 1, 0
    for j in range(N):
        if i & (1 << j):
            taste1 *= dishes[j][0]
            taste2 += dishes[j][1]
    min_val = min(min_val, (abs(taste2 - taste1)))

print(min_val)