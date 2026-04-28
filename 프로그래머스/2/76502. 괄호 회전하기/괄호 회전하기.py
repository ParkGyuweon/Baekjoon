from collections import deque

def check(candidate):
    stack = []
    for item in candidate:
        if item in ('(', '[', '{'):
            stack.append(item)
        else:
            if item == ')' and (not stack or (stack and stack.pop() != '(')):
                return False
            if item == '}' and (not stack or (stack and stack.pop() != '{')):
                return False
            if item == ']' and (not stack or (stack and stack.pop() != '[')):
                return False
    if stack:
        return False
    else:
        return True
    
def solution(s):
    answer = 0
    new_queue = deque(list(s))
    if check(new_queue):
        answer += 1
    for length in range(1, len(s)):
        new_queue.rotate(-1)
        if check(new_queue):
            answer += 1
    return answer