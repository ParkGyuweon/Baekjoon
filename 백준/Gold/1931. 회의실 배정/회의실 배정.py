import sys
input = sys.stdin.readline

N = int(input())
work = [tuple(map(int, input().split())) for _ in range(N)]
work.sort(key=lambda x:(x[1], x[0]))

turn, cur_work = 1, 0
for num in range(1, N):
    if work[num][0] >= work[cur_work][1]:
        turn += 1
        cur_work = num

print(turn)