def solution(s):
    answer = ''
    num_to_char = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    temp = ''
    for char in s:
        if char.isnumeric():
            answer = answer + char
            temp = ''
        else:
            temp = temp + char
            if temp in num_to_char:
                answer = answer + num_to_char[temp]
                temp = ''
    return int(answer)