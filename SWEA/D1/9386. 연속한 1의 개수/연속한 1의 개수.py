T = int(input())
for t in range(1, T + 1):
    N = int(input())
    number = list(map(int, input()))
    max_one = 0
    temp = []
    if number == [1]:
        max_one = 1
    elif number == [0]:
        max_one = 0
    else:
        for i in range(N - 1, -1, -1):
            if number[i] == 0:
                temp = []
                number.pop()
            else:
                temp.append(number.pop())
                if max_one < len(temp):
                    max_one = len(temp)

    print(f'#{t} {max_one}')