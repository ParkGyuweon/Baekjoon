from math import gcd

def solution(n, m):
    gcd_value = gcd(n, m)
    lcm_value = n * m // gcd_value
    answer = [gcd_value, lcm_value]
    return answer