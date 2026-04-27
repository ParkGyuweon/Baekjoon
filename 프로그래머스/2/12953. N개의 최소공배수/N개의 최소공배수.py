from math import gcd

def solution(arr):
    answer = 0
    arr.sort(reverse=True)
    cur_lcm = arr[0]
    for idx in range(1, len(arr)):
        cur_lcm = abs(cur_lcm * arr[idx]) // gcd(cur_lcm, arr[idx])
    answer = cur_lcm
    return answer