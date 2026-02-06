import sys

N = int(input())
max_val = 0
L = []

def find_max(line, idx):
    if idx == 0:
        return max(line[1], line[2], line[3], line[4])
    elif idx == 1:
        return max(line[0], line[2], line[4], line[5])
    elif idx == 2:
        return max(line[0], line[1], line[3], line[5])
    elif idx == 3:
        return max(line[0], line[2], line[4], line[5])
    elif idx == 4:
        return max(line[0], line[1], line[3], line[5])
    else:
        return max(line[1], line[2], line[3], line[4])

def opposite(idx):
    if idx == 0:
        return 5
    elif idx == 1:
        return 3
    elif idx == 2:
        return 4
    elif idx == 3:
        return 1
    elif idx == 4:
        return 2
    else:
        return 0
    
for i in range(N):
    L.append(list(map(int, sys.stdin.readline().split())))

for common in range(1, 7):
    sum = 0

    recent = common
    idx = L[0].index(recent)
    sum = sum + find_max(L[0], idx)
    opposite_idx = opposite(idx)
    recent = L[0][opposite_idx]

    for j in range(1, len(L)):
        idx = L[j].index(recent)
        sum = sum + find_max(L[j], idx)
        opposite_idx = opposite(idx)
        recent = L[j][opposite_idx]

    if max_val < sum :
        max_val = sum

print(max_val)