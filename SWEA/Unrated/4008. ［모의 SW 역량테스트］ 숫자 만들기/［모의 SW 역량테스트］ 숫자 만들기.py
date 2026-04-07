T = int(input())

def make_order(current, operators, N):
    global min_val, max_val
    if len(current) == N - 1:
        result = calc(current)
        if result == 'bad':
            return
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return

    for item in range(4):
        if operators[item] >= 1:
            current.append(item)
            operators[item] -= 1
            make_order(current, operators, N)
            current.pop()
            operators[item] += 1

def calc(combination):
    stack = [numbers[0]]
    for i in range(N - 1):
        stack.append(combination[i])
        stack.append(numbers[i + 1])
    stack.reverse()
    while len(stack) > 1:
        operand1 = stack.pop()
        operation = stack.pop()
        operand2 = stack.pop()
        if operation == 0:
            result = operand1 + operand2
        elif operation == 1:
            result = operand1 - operand2
        elif operation == 2:
            result = operand1 * operand2
        else:
            if operand2 == 0:
                return 'bad'
            result = int(operand1 / operand2)
        stack.append(result)
    return stack[0]

for t in range(1, T + 1):
    N = int(input())
    ori_operators = list(map(int,input().split()))
    numbers = list(map(int, input().split()))
    max_val, min_val = -float('inf'), float('inf')
    make_order([], ori_operators, N)
    print(f'#{t} {max_val - min_val}')
