number = sorted(list(map(int, input().split())))
while not (number[0] == 0 and number[1] == 0 and number[2] == 0):
    if number[-1] ** 2 == number[0] ** 2 + number[1] ** 2:
        print('right')
    else:
        print('wrong')
    number = sorted(list(map(int, input().split())))