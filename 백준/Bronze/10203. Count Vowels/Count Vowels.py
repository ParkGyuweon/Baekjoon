T = int(input())
for t in range(1, T + 1):
    S = input()
    print(f"The number of vowels in {S} is {S.count('a') + S.count('e') + S.count('i') + S.count('o') + S.count('u')}.")