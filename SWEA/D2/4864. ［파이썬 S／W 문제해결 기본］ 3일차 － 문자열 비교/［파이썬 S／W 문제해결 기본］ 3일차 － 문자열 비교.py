T = int(input())
for t in range(1, T + 1):
    str1 = input()
    str2 = input()
    if str1 in str2:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')