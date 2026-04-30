def word_back(current):
    global total_case
    if len(current) == 5:
        return
    
    for item in ('A', 'E', 'I', 'O', 'U'):
        current.append(item)
        total_case.append(''.join(current))
        word_back(current)
        current.pop()

total_case = []
def solution(word):
    word_back([])
    return total_case.index(word) + 1