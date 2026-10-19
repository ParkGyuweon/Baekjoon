def solution(data, col, row_begin, row_end):
    sorted_data = sorted(data, key=lambda x:(x[col-1], -x[0]))
    remaining = []
    for row in range(row_begin - 1, row_end):
        cur_remain = 0
        for number in sorted_data[row]:
            cur_remain += number % (row + 1)
        remaining.append(cur_remain)
        
    cur_answer = remaining[0]
    for remain in range(1, len(remaining)):
        cur_answer = cur_answer ^ remaining[remain]
        
    return(cur_answer)
