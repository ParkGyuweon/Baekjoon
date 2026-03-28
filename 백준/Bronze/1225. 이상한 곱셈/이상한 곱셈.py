A, B = input().split()
answer = 0

for num1 in A:
    for num2 in B:
        answer += int(num1) * int(num2)
        
print(answer)