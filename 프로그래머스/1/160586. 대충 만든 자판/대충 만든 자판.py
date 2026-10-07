def solution(keymap, targets):
    answer = []
    key_col = {}
    for key in keymap:
        for idx in range(len(key)):
            if key[idx] in key_col:
                key_col[key[idx]] = min(key_col[key[idx]], idx + 1)
            else:
                key_col[key[idx]] = idx + 1
    
    for target in targets:
        cur_answer = 0
        for char in target:
            if char not in key_col:
                cur_answer = -1
                break
            else:
                cur_answer += key_col[char]
        answer.append(cur_answer)
    return answer