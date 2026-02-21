import sys
input = sys.stdin.readline

N = int(input())
opinion = sorted([int(input()) for _ in range(N)])
if N == 0:
    print(0)
else:
    if (0.15 * N) - 0.5 >= int(0.15 * N):
        people = int(0.15 * N) + 1
    else:
        people = int(0.15 * N)
    total_people = N - 2 * people
    sum_val = sum(opinion[people : N - people])
    average = sum_val / total_people
    if average - 0.5 >= int(average):
        print(int(average) + 1)
    else:
        print(int(average))