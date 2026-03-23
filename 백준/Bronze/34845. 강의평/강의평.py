N, X = map(int, input().split())
scores = list(map(int, input().split()))
cur_sum, cur_length, answer = sum(scores), len(scores), 0

while cur_sum / cur_length < X:
    answer += 1
    cur_sum += 100
    cur_length += 1
print(answer)