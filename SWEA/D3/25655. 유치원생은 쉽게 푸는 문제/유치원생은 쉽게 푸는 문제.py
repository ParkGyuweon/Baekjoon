T = int(input())

for i in range(T):
    N = int(input())
    if N % 2 == 0:
        value = '8' * (N // 2)
    else:
        if N == 1:
            value = 0
        elif N == 3:
            value = 48
        else:
            value = '48' + ('8' * ((N - 3) // 2))
    print(value)