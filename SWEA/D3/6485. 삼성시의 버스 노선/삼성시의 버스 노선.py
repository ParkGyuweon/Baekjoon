T = int(input())
for t in range(1, T + 1):
    N = int(input())
    number_AB = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    number_C = [int(input()) for _ in range(P)]
    print(f'#{t} ', end = '')
    for i in number_C:
        number = 0
        for A, B in number_AB:
            if A <= i <= B:
                number = number + 1

        print(number, end = ' ')
    print()