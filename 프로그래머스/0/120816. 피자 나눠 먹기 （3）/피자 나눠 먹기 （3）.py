def solution(slice, n):
    if n / slice != n // slice:
        answer = n // slice + 1
    else:
        answer = n // slice
    return answer