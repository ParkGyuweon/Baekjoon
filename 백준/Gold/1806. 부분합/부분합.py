N, S = map(int, input().split())
number_list = list(map(int, input().split()))
start, end, cur_sum, min_len = 0, 0, 0, 10E10
while start <= N - 1 and end <= N - 1:
    cur_sum += number_list[end]
    if cur_sum >= S:
        while cur_sum >= S:
            cur_sum -= number_list[start]
            start += 1
        min_len = min(min_len, (end - start + 2))
    end += 1
if cur_sum >= S:
    min_len = min(min_len, (end - start + 1))
if min_len == 10E10:
    print(0)
else:
    print(min_len)