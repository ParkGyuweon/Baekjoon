import sys
input = sys.stdin.readline

N = int(input().strip())
stack = []
def op(string):
    if ' ' in string:
        stack.append(int(string.split()[1]))
        return
    if string == 'pop':
        if not stack:
            print(-1)
        else:
            number = stack[-1]
            del stack[-1]
            print(number)
        return
    if string == 'size':
        print(len(stack))
    if string == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
        return
    if string == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
        return

for i in range(N):
    op(input().strip())