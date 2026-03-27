N = int(input())
number_list = list(map(int, input().split()))
inc_list = [0] * N
dec_list = [0] * N
total_num = [1] * N
bi_flag, num = False, 0
max_len = 0

for num1 in range(N):
    inc_list[num1] = 1
    dec_list[N - num1 -1] = 1
    for num2 in range(num1):
        if number_list[num2] < number_list[num1]:
            inc_list[num1] = max(inc_list[num1], inc_list[num2] + 1)
        if number_list[N - num2 -1] < number_list[N - num1 -1]:
            dec_list[N - num1 -1] = max(dec_list[N - num1 -1], dec_list[N - num2 -1] + 1)
for num in range(N):
    max_len = max(max_len, inc_list[num] + dec_list[num])

print(max_len - 1)