import sys
input = sys.stdin.readline

S = input().strip()
Q = int(input().strip())
alpha_dict = {'a': [0] * (len(S) + 1), 'b': [0] * (len(S) + 1), 'c': [0] * (len(S) + 1), 'd': [0] * (len(S) + 1),
              'e': [0] * (len(S) + 1), 'f': [0] * (len(S) + 1), 'g': [0] * (len(S) + 1), 'h': [0] * (len(S) + 1),
              'i': [0] * (len(S) + 1), 'j': [0] * (len(S) + 1), 'k': [0] * (len(S) + 1), 'l': [0] * (len(S) + 1),
              'm': [0] * (len(S) + 1), 'n': [0] * (len(S) + 1), 'o': [0] * (len(S) + 1), 'p': [0] * (len(S) + 1),
              'q': [0] * (len(S) + 1), 'r': [0] * (len(S) + 1), 's': [0] * (len(S) + 1), 't': [0] * (len(S) + 1),
              'u': [0] * (len(S) + 1), 'v': [0] * (len(S) + 1), 'w': [0] * (len(S) + 1), 'x': [0] * (len(S) + 1),
              'y': [0] * (len(S) + 1), 'z': [0] * (len(S) + 1)}

for char in range(len(S)):
    if char == 0:
        alpha_dict[S[char]][char + 1] += 1
        continue
    for alpha in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'):
        alpha_dict[alpha][char + 1] = alpha_dict[alpha][char]
    alpha_dict[S[char]][char + 1] += 1

for _ in range(Q):
    cur_char, start, end = input().split()
    print(alpha_dict[cur_char][int(end) + 1] - alpha_dict[cur_char][int(start)])