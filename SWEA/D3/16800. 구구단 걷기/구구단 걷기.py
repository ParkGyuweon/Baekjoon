T = int(input())

for i in range(T):
    N = int(input())
    A = 0
    B = 0
    min_value = 10E10
    for j in range(1, int((N) ** 0.5) + 1):
        if N % j == 0:
            A = j
            B = N // j
            if (A + B - 2) < min_value:
            	min_value = A + B - 2
    print(f'#{i + 1} {A + B - 2}')     