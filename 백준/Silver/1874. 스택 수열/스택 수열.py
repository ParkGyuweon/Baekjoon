N = int(input())
result = list(int(input()) for _ in range(N))
number = list(range(1, N + 1))
stack = [0]
answer = []

while result:
    if stack[-1] < result[0]:
        while stack[-1] != result[0]:
            stack.append(number.pop(0))
            answer.append('+')
    elif stack[-1] == result[0]:
        stack.pop()
        result.pop(0)
        answer.append('-')
    elif result and stack[-1] > result[0]:
        print('NO')
        break
else:
    print('\n'.join(answer))