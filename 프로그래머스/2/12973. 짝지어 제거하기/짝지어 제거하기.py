def solution(s):
    idx = 0
    stack = []
    while idx < len(s):
        stack.append(s[idx])
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
        idx += 1
        
    if not stack:
        answer = 1
    else:
        answer = 0
    return answer