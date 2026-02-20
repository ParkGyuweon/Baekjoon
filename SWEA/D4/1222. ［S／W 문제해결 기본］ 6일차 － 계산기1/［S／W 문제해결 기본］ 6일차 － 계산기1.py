icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}

for t in range(1, 11):
    N = int(input())
    stack = [0] * (N + 1)
    infix = input()
    top = -1
    postfix = ''

    for token in infix:
        if token not in '*/+-':
            postfix += token
        else:
            if top == -1 or isp[stack[top]] < icp[token]:
                top += 1
                stack[top] = token
            elif isp[stack[top]] >= icp[token]:
                while top > -1 and isp[stack[top]] >= icp[token]:
                    top -= 1
                    postfix += stack[top + 1]
                top += 1
                stack[top] = token

    while top > -1:
        top -= 1
        postfix += stack[top + 1]

    stack = []
    for token in postfix:
        if token in '+-/*':
            if len(stack) < 2:
                print(f'#{t} error')
                break
            else:
                second = stack.pop()
                first = stack.pop()
                if token == '+':
                    stack.append(first + second)
                elif token == '-':
                    stack.append(first - second)
                elif token == '*':
                    stack.append(first * second)
                elif token == '/':
                    stack.append(first // second)
        else:
            stack.append(int(token))

    print(f'#{t} {stack.pop()}')