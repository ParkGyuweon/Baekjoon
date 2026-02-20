from collections import defaultdict

T = int(input())
for t in range(1, T + 1):
    test_case, length = map(str, input().split())
    num_list = input()
    number = defaultdict(int)
    strange = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    print(test_case)
    for i in range(10):
        number[i] = num_list.count(strange[i])
        for j in range(number[i]):
            print(strange[i], end = ' ')
    print()