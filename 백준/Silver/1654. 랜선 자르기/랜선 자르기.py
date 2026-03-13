import sys
input = sys.stdin.readline
K, N = map(int, input().split())
line_list = [int(input()) for _ in range(K)]
line_list.sort(reverse=True)
start, end, result = 1, max(line_list), 0

while start <= end:
    mid = (start + end) // 2
    cur_sum = 0
    for item in line_list:
        if item < mid:
            break
        cur_sum += item // mid
    if cur_sum >= N:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)