T = int(input())
str_16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
for t in range(1,  T + 1):
    print(f'#{t}', end=' ')
    N, current = input().split()
    N = int(N)
    for i in range(N):
        cur_ten = str_16.index(current[i])
        cur_2 = []
        while cur_ten != 0:
            cur_2.insert(0, cur_ten % 2)
            cur_ten = cur_ten // 2
        while len(cur_2) < 4:
            cur_2.insert(0, 0)
        print(''.join(map(str, cur_2)), end = '')
    print()