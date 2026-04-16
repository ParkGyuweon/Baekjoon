from collections import defaultdict
books = defaultdict(int)
N = int(input())

for _ in range(N):
    book = input()
    books[book] += 1
    
book_list = sorted(list(books.items()), key=lambda x:(-x[1], x[0]))
print(book_list[0][0])