A = int(input())
B = int(input())
C = int(input())
total = str(A * B * C)
number = [0] * 10
for i in range(len(total)):
    number[int(total[i])] += 1
print('\n'.join(map(str, number)))