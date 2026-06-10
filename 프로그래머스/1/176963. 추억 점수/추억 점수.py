def solution(name, yearning, photo):
    score_dict = {}
    for idx in range(len(name)):
        score_dict[name[idx]] = yearning[idx]
    
    answer = []
    for pic in photo:
        cur_val = 0
        for name in pic:
            if name in score_dict:
                cur_val += score_dict[name]
        answer.append(cur_val)
    return answer