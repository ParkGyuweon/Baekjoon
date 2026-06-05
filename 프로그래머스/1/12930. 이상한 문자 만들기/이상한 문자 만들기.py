def solution(s):
    idx = 0
    answer = ''
    for total_idx in range(len(s)):
        if s[total_idx] == ' ':
            idx = 0
            answer += ' '
            continue
        else:
            if idx % 2 == 0:
                answer += s[total_idx].upper()
            else:
                answer += s[total_idx].lower()
            idx += 1
    return answer