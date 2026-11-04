N = int(input())

# Please write your code here.
if N == 1:
    print(1)
elif N == 2:
    print(1)
else:
    fibonachi = [0] * N
    fibonachi[0], fibonachi[1] = 1, 1
    for idx in range(2, N):
        fibonachi[idx] = fibonachi[idx - 1] + fibonachi[idx - 2]
    print(fibonachi[-1])
