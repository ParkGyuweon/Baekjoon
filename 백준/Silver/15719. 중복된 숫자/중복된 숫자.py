import sys
N = int(input())
one_line = sys.stdin.readline()
sum_val, one_char = 0, ''

for item in one_line:
    if item not in (' ', '\n'):
        one_char += item
    else:
        sum_val += int(one_char)
        one_char = ''
print(sum_val - sum(range(1, N)))