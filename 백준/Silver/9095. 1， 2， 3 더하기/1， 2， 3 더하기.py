T = int(input())
number_list = [1, 2, 3]

def check(number_list, current, n):
    global case_num
    if sum(current) == n:
        case_num += 1
        return
    if sum(current) > n:
        return
    for num in number_list:
        current.append(num)
        check(number_list, current, n)
        current.pop()

for t in range(1, T + 1):
    n = int(input())
    case_num = 0
    check(number_list, [], n)
    print(case_num)