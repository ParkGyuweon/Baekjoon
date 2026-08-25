from math import gcd

def solution(n):
    answer = n * 6 // gcd(n, 6)
    return answer // 6