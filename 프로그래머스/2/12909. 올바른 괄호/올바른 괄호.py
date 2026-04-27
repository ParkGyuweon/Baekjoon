def solution(s):
    stack = []
    for item in s:
        if item == '(':
            stack.append('(')
        elif item == ')':
            if not stack:
                return False
            if stack.pop() == ')':
                return False
    if stack:
        return False
    return True