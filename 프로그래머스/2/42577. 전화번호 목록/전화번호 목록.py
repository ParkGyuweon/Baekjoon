def solution(phone_book):
    phone_book.sort(key=lambda x:len(x))
    phone_book.sort()
    for idx in range(1, len(phone_book)):
        if phone_book[idx - 1] == phone_book[idx][:len(phone_book[idx - 1])]:
            return False
    return True