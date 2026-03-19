from collections import deque

S = input()
operation_num = S.count('+') + S.count('-')
total_stack = deque([''] * (operation_num * 2 + 1))
idx = 0
for num in range(len(S)):
    if S[num] in ('+', '-'):
        idx += 1
        total_stack[idx] += S[num]
        idx += 1
    else:
        total_stack[idx] += S[num]

result_stack, idx = deque(), 0
while total_stack:
    cur_char = total_stack.popleft()
    if cur_char == '+':
        result_stack.append(int(result_stack.pop()) + int(total_stack.popleft()))
    else:
        result_stack.append(cur_char)

final_stack = []
while len(result_stack) >= 1:
    cur_char = result_stack.popleft()
    if cur_char == '-':
        final_stack.append(int(final_stack.pop()) - int(result_stack.popleft()))
    else:
        final_stack.append(cur_char)

print(final_stack[0])