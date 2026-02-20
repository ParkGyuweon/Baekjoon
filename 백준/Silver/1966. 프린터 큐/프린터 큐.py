T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    paper = list(map(int, input().split()))
    number = 0
    for i in range(N):
        paper[i] = (paper[i], i)
    while True:
        for i in range(1, len(paper)):
            if paper[0][0] < paper[i][0]:
                paper.append(paper.pop(0))
                break
        else:
            current = paper.pop(0)
            number += 1
            if current[1] == M:
                print(number)
                break
