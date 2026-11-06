from collections import defaultdict

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

# Please write your code here.
number_cnt = defaultdict(int)
for number in numbers:
    number_cnt[number] += 1

answer = sorted(list(number_cnt.items()), key=lambda x:(-x[1], -x[0]))
for idx in range(K):
    print(answer[idx][0], end = ' ')