T = int(input())
for t in range(1, T + 1):
    postfix = list(input().split())
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
        elif token == '.':
            if len(stack) == 1:
                print(f'#{t} {stack.pop()}')
            else:
                print(f'#{t} error')
        else:
            stack.append(int(token))