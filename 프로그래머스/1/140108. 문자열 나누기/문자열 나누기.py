from collections import deque

def solution(s):
    s = deque(s)
    answer = 1
    cur_x = s[0]
    same, diff = 0, 0
    while len(s) > 0:
        while s:
            if cur_x == s.popleft():
                same += 1
            else:
                diff += 1
            if same == diff and s:
                cur_x = s[0]
                answer += 1
                if len(s) == 0:
                    return answer
                break
    return answer