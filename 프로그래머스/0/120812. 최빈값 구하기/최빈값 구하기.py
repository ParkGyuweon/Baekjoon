def solution(array):
    cnt_list = [0] * 1001
    for num in array:
        cnt_list[num] += 1
    max_val = max(cnt_list)
    if cnt_list.count(max_val) > 1:
        return -1
    else:
        return cnt_list.index(max_val)