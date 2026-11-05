from collections import defaultdict

N = int(input())
words = [input() for _ in range(N)]
word_count = defaultdict(int)
# Please write your code here.

for word in words:
    word_count[word] += 1

word_count = sorted(list(word_count.items()), key=lambda x:x[1])
print(word_count[-1][1])