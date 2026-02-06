import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input().strip())
L = []
for i in range(T):
    L.append(int(input().strip()))
fibo = [0] * max(L)
if max(L) > 1:
    fibo[0] = 1
    fibo[1] = 1
def fibonachi():
    for i in range(2, len(fibo)):
        fibo[i] = fibo[i - 1] + fibo[i - 2]

fibonachi()
for i in L:
    if i == 0:
        print('1 0\n')
    elif i == 1:
        print('0 1\n')
    else:
        print(str(fibo[i - 2]) + ' ' + str(fibo[i - 1]) + '\n')