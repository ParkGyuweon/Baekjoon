from heapq import heappop, heappush

def solution(operations):
    answer = []
    min_heapq = []
    max_heapq = []
    idx_check = [0] * len(operations)
    add_num, pop_num = 0, 0
    for operation_idx in range(len(operations)):
        operation = operations[operation_idx]
        command, number = operation.split()
        if command == 'I':
            add_num += 1
            heappush(min_heapq, (int(number), operation_idx))
            heappush(max_heapq, (-1 * int(number), operation_idx))
            idx_check[operation_idx] = 1
        elif add_num > pop_num and min_heapq and command == 'D' and number[0] == '-':
            pop_num += 1
            cur_number, cur_idx = heappop(min_heapq)
            while min_heapq and idx_check[cur_idx] == 0:
                cur_number, cur_idx = heappop(min_heapq)
            idx_check[cur_idx] = 0
        elif add_num > pop_num and max_heapq and command == 'D' and number[0] != '-':
            pop_num += 1
            cur_number, cur_idx = heappop(max_heapq)
            while max_heapq and idx_check[cur_idx] == 0:
                cur_number, cur_idx = heappop(max_heapq)
            idx_check[cur_idx] = 0
        
    if add_num == pop_num:
        return [0, 0]
    else:
        cur_max, cur_idx = heappop(max_heapq)
        while max_heapq and idx_check[cur_idx] == 0:
            cur_max, cur_idx = heappop(max_heapq)
        cur_min, cur_idx = heappop(min_heapq)
        while min_heapq and idx_check[cur_idx] == 0:
            cur_min, cur_idx = heappop(min_heapq)
        return [-1 * cur_max, cur_min]