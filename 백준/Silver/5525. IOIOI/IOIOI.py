N = int(input())
M = int(input())
S = input()

current = 'IOI' + ("OI" * (N - 1))
result = 0
for num in range(M - len(current) + 1):
    if S[num: num + len(current)] == current:
        result += 1

print(result)