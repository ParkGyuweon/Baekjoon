T = int(input())

def make_top(cur_sum, start):
    global min_height_sum
    if cur_sum - B >= min_height_sum:
        return

    if cur_sum >= B:
        min_height_sum = min(min_height_sum, cur_sum - B)
        return

    if start == N:
        return

    for person in range(start, N):
        make_top(cur_sum + height_list[person], person + 1)

for t in range(1, T + 1):
    N, B = map(int, input().split())
    height_list = list(map(int, input().split()))

    min_height_sum = 10E10
    make_top(0, 0)
    print(f'#{t} {min_height_sum}')