N = int(input())
max_score = 0
score_list = [int(input()) for _ in range(N)]

if N == 1:
    print(score_list[0])
elif N == 2:
    print(score_list[0] + score_list[1])
else:
    memory = [0] * N
    memory[0] = score_list[0]
    memory[1] = score_list[0] + score_list[1]
    memory[2] = max(score_list[0] + score_list[2], score_list[1] + score_list[2])

    for i in range(3, N):
        memory[i] = max(memory[i - 2] + score_list[i], memory[i - 3] + score_list[i - 1] + score_list[i])

    print(memory[N - 1])