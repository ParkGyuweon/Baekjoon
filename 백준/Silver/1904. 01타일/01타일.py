import sys
input = sys.stdin.readline

N = int(input().strip())
if N == 1:
    print(1)
elif N == 2:
    print(2)
elif N == 3:
    print(3)
else:
    first_num, second_num = 2, 3

    for num in range(3, N):
        new_num = (first_num + second_num) % 15746
        first_num, second_num = second_num, new_num
    print(second_num)