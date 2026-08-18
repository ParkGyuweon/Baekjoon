from math import gcd

def solution(numer1, denom1, numer2, denom2):
    lcm_val = (denom1 * denom2) // gcd(denom1, denom2)
    answer_numer = numer1 * (lcm_val // denom1) + numer2 * (lcm_val // denom2)
    answer_demer = lcm_val
    answer = [answer_numer // gcd(answer_numer, answer_demer), answer_demer // gcd(answer_numer, answer_demer)]
    return answer