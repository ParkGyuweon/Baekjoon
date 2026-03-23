T = int(input())

for t in range(1, T + 1):
    num1, num2 = input().split()
    total_sum = int(num1, 2) + int(num2, 2)
    print(bin(total_sum)[2:])