N = int(input())

def hanoi_count(N):
    if N == 1:
        return 1
    return  2 * hanoi_count(N - 1) + 1

def hanoi_act(N, start, end, sub):
    if N == 1:
        return print(start, end)
    hanoi_act(N - 1, start, sub, end)
    print(start, end)
    hanoi_act(N - 1, sub, end, start)

num = hanoi_count(N)
print(num)
hanoi_act(N, 1, 3, 2)
