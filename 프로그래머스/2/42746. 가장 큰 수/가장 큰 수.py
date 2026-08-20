from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(lambda a, b: int(b + a) - int(a + b)))
    answer = ''.join(numbers)
    if answer[0] == '0':
        return "0"
    return answer