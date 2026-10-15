def solution(babbling):
    answer = 0
    words = {'aya' : 0, 'ye' : 1, 'woo' : 2, 'ma' : 3}
    for word in babbling:
        cur_word, idx, cur_part, prev = word, 0, '', -1
        while cur_word and idx < len(cur_word):
            cur_part += cur_word[idx]
            idx += 1
            if cur_part in ['aya', 'ye', 'woo', 'ma'] and words[cur_part] != prev:
                cur_word = cur_word[idx:]
                prev = words[cur_part]
                cur_part = ''
                idx = 0
                
        if not cur_word and not cur_part:
            answer += 1
        
    return answer