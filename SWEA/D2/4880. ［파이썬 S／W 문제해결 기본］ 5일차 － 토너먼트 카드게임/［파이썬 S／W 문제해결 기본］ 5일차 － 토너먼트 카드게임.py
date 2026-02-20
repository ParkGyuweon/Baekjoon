T = int(input())

def rsp(num1, item1, num2, item2):
    if item1 == item2:
        if num1 < num2:
            return num1
        return num2
    if (item1, item2) in [(1, 3), (2, 1), (3, 2)] :
    	return num1
    return num2

def tonerment(combination):
    if len(combination) == 1:
        return combination[0]
    if len(combination) == 2:
        return rsp(combination[0], cards[combination[0] - 1], combination[1], cards[combination[1] - 1])
    return tonerment([tonerment(combination[0 : (1 + len(combination)) // 2])] + [tonerment(combination[(1 + len(combination)) // 2 : len(combination)])])

for t in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    current = [n for n in range(1, N + 1)]
    print(f'#{t} {tonerment(current)}')