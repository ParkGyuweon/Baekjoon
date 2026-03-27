N = int(input())
# 1이면 1 2 3 4 5 6 7 8 9
# 2이면 12 10 21 23 32 35 43 45 54 56 65 67 76 78 87 89 98 -> 9 * 2 - 1 = 17
# 3이면 121 123 101 212 210 232 234 323 321 345 343 434 432 456 454 543 545 565 567 654 656 678 676 765 767 789 787 876
# 878 898 987 989 -> 32 = 17 * 2 - 2
num_list = [1] * 10
num_list[0] = 0
for idx in range(1, N):
    new_list = [num_list[1], num_list[0] + num_list[2], num_list[1] + num_list[3], num_list[2] + num_list[4],
                num_list[3] + num_list[5], num_list[4] + num_list[6], num_list[5] + num_list[7],
                num_list[6] + num_list[8], num_list[7] + num_list[9], num_list[8]]
    num_list = new_list

print(sum(num_list) % 1000000000)