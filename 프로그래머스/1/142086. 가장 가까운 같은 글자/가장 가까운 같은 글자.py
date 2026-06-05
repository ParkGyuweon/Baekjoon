from collections import defaultdict

def solution(s):
    char_list = defaultdict(int)
    answer = []
    for idx in range(len(s)):
        if s[idx] not in char_list:
            answer.append(-1)
            char_list[s[idx]] = idx
        else:
            answer.append(idx - char_list[s[idx]])
            char_list[s[idx]] = idx
    return answer