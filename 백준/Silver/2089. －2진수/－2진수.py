N = int(input())
if N == 0:
    print(0)
else:
    answer = ''
    first_num = 1
    while N != 0:
        if N % -2 == -1:
            answer += str(N % (-2) * -1)
            N -= 2
        else:
            answer += str(N % (-2))
        N = N // (-2)

    print(answer[::-1])