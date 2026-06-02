def solution(s):
    lower_s = ''
    upper_s = ''
    for char in s:
        if char.isupper():
            upper_s += char
        else:
            lower_s += char

    return ''.join(sorted(lower_s, reverse=True) + sorted(upper_s, reverse=True))