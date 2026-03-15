N, S = map(int, input().split())
number = list(map(int, input().split()))
answer = 0

for i in range(1, 1 << N):
    current = 0
    for j in range(N):
        if i & (1 << j):
            current += number[j]
    if current == S:
        answer += 1
print(answer)