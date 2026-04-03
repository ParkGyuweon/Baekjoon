N = int(input())
numbers = {0 : 0, 1 : 1, 2 : 1, 3 : 2, 4 : 3, 5 : 5}

def fibonachi(num):
    if num in numbers:
        return numbers[num]
    elif num % 2 == 0:
        numbers[num] = (fibonachi(num // 2) * (fibonachi(num // 2 - 1) * 2 + fibonachi((num // 2)))) % 1000000007
    else:
        numbers[num] = (fibonachi(num // 2 + 1) ** 2 + fibonachi(num // 2) ** 2) % 1000000007
    return numbers[num]

fibonachi(N)
print(numbers[N])