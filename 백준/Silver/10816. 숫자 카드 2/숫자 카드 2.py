from bisect import bisect_left, bisect_right

def calCountsByRange(nums, left_value, right_value):
    r_i = bisect_right(nums, right_value)
    l_i = bisect_left(nums, left_value)
    return r_i - l_i

N = int(input())
L_N = list(map(int, input().split()))
M = int(input())
L_M = list(map(int, input().split()))

L_N.sort()
L_result = []
for i in L_M:
    print(calCountsByRange(L_N, i, i), end = ' ')
