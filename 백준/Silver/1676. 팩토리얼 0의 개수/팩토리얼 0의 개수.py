N = int(input())
number = [1]
def factorial(N):
    for i in range(2, N + 1):
        number.append(i * number[-1])
    return number[-1]
if N == 0 or N == 1:
    print(0)
else:
    answer = factorial(N)
    number = 0
    idx = len(str(answer)) - 1
    while str(answer)[idx] == '0':
        number += 1
        idx = idx - 1
    print(number)
