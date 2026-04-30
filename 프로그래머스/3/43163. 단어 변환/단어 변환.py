from collections import deque

def solution(begin, target, words):
    queue = deque([(begin, 0)])
    word_set = {begin}
    if target not in words:
        return 0
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while queue:
        cur_word, cur_turn = queue.popleft()
        for item in range(len(cur_word)):
            for alphabet in alphabets:
                new_word = list(cur_word)
                if alphabet != cur_word[item]:
                    new_word[item] = alphabet
                    new_string = ''.join(new_word)
                    if new_string not in word_set and new_string in words:
                        if new_string == target:
                            return cur_turn + 1
                        word_set.add(new_string)
                        queue.append((new_string, cur_turn + 1))
                
    return 0