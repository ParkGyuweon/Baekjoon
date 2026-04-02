for _ in range(3):
    one_line = list(map(int, input().split()))
    if sum(one_line) == 1:
        print('C')
    elif sum(one_line) == 2:
        print('B')
    elif sum(one_line) == 3:
        print('A')
    elif sum(one_line) == 4:
        print('E')
    else:
        print('D')