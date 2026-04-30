def check_prime(number):
    if number == 1:
        return False
    for num in range(2, int(number ** (1/2)) + 1):
        if number % num == 0:
            return False
    return True

def solution(n, k):
    answer = ''
    while n != 0:
        answer += str(n % k)
        n = n // k
    answer = answer[::-1]
    prime_list = list(answer.split('0'))
    result = 0
    for item in prime_list:
        if item and check_prime(int(item)):
            result += 1
    return result