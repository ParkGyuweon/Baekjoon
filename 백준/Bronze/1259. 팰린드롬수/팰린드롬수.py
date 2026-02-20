num = input()
while num != '0':
    for i in range(len(num) // 2):
        if num[i] != num[-(i + 1)]:
            print('no')
            break
    else:
        print('yes')
    num = input()