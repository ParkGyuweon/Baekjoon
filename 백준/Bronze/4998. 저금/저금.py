while True:
    try:
        N, B, M = map(float, input().split())
        answer = 0
        while N < M:
            N = N + (N * B * 0.01)
            answer += 1
        print(answer)
    except EOFError:
        exit()