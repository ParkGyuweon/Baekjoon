from collections import defaultdict

N, K = map(int, input().split())
numbers = list(map(int, input().split()))
number_cnt = defaultdict(int)
# Please write your code here.
for number in numbers:
    number_cnt[number] += 1
answer = 0

for key, value in number_cnt.items():
    if (K - key) == key:
        answer += value * (value - 1)
    elif (K - key) in number_cnt:
        answer += value * number_cnt[K - key]

print(answer // 2)