from collections import deque

def solution(s):
    total_list = set()
    s_list = deque(s[1:-1])
    while s_list:
        cur_char = s_list.popleft()
        if cur_char == '{':
            cur_s = ''
            cur_char = s_list.popleft()
            while cur_char != '}':
                cur_s += cur_char
                cur_char = s_list.popleft()
        cur_item = tuple(map(int, list(cur_s.split(','))))
        total_list.add(cur_item)
    
    total_list = sorted(list(total_list), key=lambda x:len(x))
    answer = []
    answer_set = set()
    for item in total_list:
        for char in item:
            if char not in answer_set:
                answer.append(char)
                answer_set.add(char)
        
    return answer