import sys
input = sys.stdin.readline

M = int(input().strip())
number_cnt = [0] * 20

for i in range(M):
    command = input().strip().split()
    if len(command) >= 2:
        if command[0] == 'add':
            if number_cnt[int(command[1]) - 1] == 0:
                number_cnt[int(command[1]) - 1] = 1
        elif command[0] == 'remove':
            if number_cnt[int(command[1]) - 1] >= 1:
                number_cnt[int(command[1]) - 1] -= 1
        elif command[0] == 'check':
            if number_cnt[int(command[1]) - 1] >= 1:
                print(1)
            else:
                print(0)
        elif command[0] == 'toggle':
            if number_cnt[int(command[1]) - 1] >= 1:
                number_cnt[int(command[1]) - 1] = 0
            else:
                number_cnt[int(command[1]) - 1] += 1
    else:
        if command[0] == 'all':
            for num in range(20):
                number_cnt[num] = 1
        elif command[0] == 'empty':
            for num in range(20):
                number_cnt[num] = 0