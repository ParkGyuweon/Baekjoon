def number_back(current, start, numbers, visited, total_set):
    global answer
    if current:
        real_current = ''
        for item in current:
            real_current = real_current + numbers[item]
        
        for num in range(2, (int(int(real_current) ** (1/2)) + 1)):
            if int(real_current) % num == 0:
                break
        else:
            if int(real_current) != 0 and int(real_current) != 1:
                total_set.add(int(real_current))
    
    if len(current) == len(numbers):
        return
    
    for idx in range(len(numbers)):
        if visited[idx]:
            continue
        visited[idx] = 1
        number_back(current + [idx], start + 1, numbers, visited, total_set)
        visited[idx] = 0
                
answer = 0
def solution(numbers):
    total_set = set()
    visited = [0] * len(numbers)
    number_back([], 0, numbers, visited, total_set)
    print(total_set)
    return len(total_set)