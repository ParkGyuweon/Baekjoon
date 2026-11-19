def solution(s, skip, index):
    answer = ''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for char in s:
        idx, cur_char = 0, alphabet.index(char)
        while idx < index:
            if alphabet[(cur_char + 1) % len(alphabet)] in skip:
                cur_char += 1
            else:
                cur_char += 1
                idx += 1
        answer += alphabet[cur_char % len(alphabet)]
    return answer