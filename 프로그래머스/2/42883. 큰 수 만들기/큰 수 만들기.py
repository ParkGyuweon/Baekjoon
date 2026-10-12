def solution(number, k):
    cur_delete = 0
    stack = []
    number = list(map(int, number))
    for num in number:
        if not stack or stack[-1] >= num:
            stack.append(num)
        elif cur_delete == k:
            stack.append(num)
        elif stack[-1] < num:
            while stack and stack[-1] < num and cur_delete < k:
                stack.pop()
                cur_delete += 1
            stack.append(num)
    
    if cur_delete != k:
        while cur_delete < k:
            stack.pop()
            cur_delete += 1
            
    return ''.join(list(map(str, stack)))