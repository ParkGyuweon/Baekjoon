N = int(input())
electronic = [tuple(map(int, input().split())) for _ in range(N)]
electronic.sort(key=lambda x:x[0])
count_list = [1] * N

for num1 in range(N):
    for num2 in range(num1):
        if electronic[num2][1] < electronic[num1][1]:
            count_list[num1] = max(count_list[num1], count_list[num2] + 1)
print(N - max(count_list))