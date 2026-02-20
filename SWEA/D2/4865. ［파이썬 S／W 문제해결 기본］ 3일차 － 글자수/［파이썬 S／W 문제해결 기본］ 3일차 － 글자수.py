T = int(input())
for t in range(1, T + 1):
    max_val = 0
    str1 = set(input())
    str2 = input()
    for char1 in str1:
        cnt = 0
        for char2 in str2:
            if char1 == char2:
                cnt = cnt + 1
        if cnt > max_val:
            max_val = cnt
    print(f'#{t} {max_val}')