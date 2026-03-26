N, D = map(int, input().split())
direction = [{'d' : 'q', 'b' : 'p', 'q' : 'd', 'p' : 'b'},
             {'d': 'b', 'b' : 'd', 'q' : 'p', 'p' : 'q'}]

for _ in range(N):
    S = input()
    answer = ''
    for item in S:
        answer += direction[D - 1][item]
    print(answer)