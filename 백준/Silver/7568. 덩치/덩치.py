N = int(input())
person = sorted([tuple(map(int, (input() + f' {i}').split())) for i in range(N)])
score = [1] * N
for i in range(N):
    for j in range(i + 1, N):
        if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            score[person[i][2]] += 1
print(' '.join(map(str, score)))
