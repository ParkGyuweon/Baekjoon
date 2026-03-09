N = int(input())
number = list(map(int, input().split()))
sort_ver = list(sorted(set(number)))
number_cnt = [1] * (N + 1) # i번째 원소를 마지막으로 하는 부분 수열의 크기

for i in range(N):
    for j in range(i):
        if number[j] < number[i]:
            number_cnt[i] = max(number_cnt[i], number_cnt[j] + 1)

print(max(number_cnt))