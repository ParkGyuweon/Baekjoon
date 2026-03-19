T = int(input())

for t in range(1, T + 1):
    commands = list(input())
    N = int(input())
    number_list = list(input().strip('[').strip(']').split(','))
    R_cnt = 0
    left_cnt, right_cnt = 0, 0
    for command in commands:
        if command == 'R':
            R_cnt += 1
        elif command == 'D' and R_cnt % 2 == 0:
            left_cnt += 1
        elif command == 'D' and R_cnt % 2 == 1:
            right_cnt += 1
    if left_cnt + right_cnt > N:
        print('error')
    else:
        if R_cnt % 2 == 0:
            print('[' + ','.join(number_list[left_cnt: N - right_cnt]) + ']')
        else:
            print('[' + ','.join(number_list[left_cnt : N - right_cnt][::-1]) + ']')