from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0)])
    answer = 0
    while queue:
        cur_number, cur_operation = queue.popleft()
        if cur_operation == len(numbers) - 1 and cur_number + numbers[cur_operation] == target:
            answer += 1
        elif cur_operation + 1 < len(numbers):
            queue.append((cur_number + numbers[cur_operation], cur_operation + 1))
            
        if cur_operation == len(numbers) - 1 and cur_number - numbers[cur_operation] == target:
            answer += 1
        elif cur_operation + 1 < len(numbers):
            queue.append((cur_number - numbers[cur_operation], cur_operation + 1))
            
    return answer