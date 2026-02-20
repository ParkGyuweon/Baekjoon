N = int(input())
stack = []

for i in range(N):
    one_line = list(input().split())
    if one_line[0] == 'push':
        stack.append(int(one_line[1]))
    elif one_line[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop(0))
    elif one_line[0] == 'size':
        print(len(stack))
    elif one_line[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif one_line[0] == 'front':
        if not stack:
            print(-1)
        else:
            print(stack[0])
    elif one_line[0] == 'back':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
