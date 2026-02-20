T = int(input())
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for i in range(T):
    A, B = map(str, input().split())
    if A == B:
        print('E')
    elif abs(colors.index(A) - colors.index(B)) == 1 or abs(colors.index(A) - colors.index(B)) == 5:
        print('A')
    elif abs(colors.index(A) - colors.index(B)) == 3:
        print('C')
    else:
        print('X')