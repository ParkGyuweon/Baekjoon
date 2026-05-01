def solution(numbers):
    answer = [-1] * len(numbers)
    pending_list = []
    pending_idx = []
    for idx in range(len(numbers)):
        for item_idx in range(len(pending_list)):
            cur_item, cur_idx = pending_list.pop(), pending_idx.pop()
            if numbers[idx] < cur_item:
                answer[cur_idx] = idx - cur_idx
                
            else:
                pending_list.append(cur_item)
                pending_idx.append(cur_idx)
                break 
                
        pending_list.append(numbers[idx])
        pending_idx.append(idx)
    for item_idx in range(len(pending_list)):
        cur_item, cur_idx = pending_list.pop(), pending_idx.pop()
        answer[cur_idx] = idx - cur_idx
        
    return answer