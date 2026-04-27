def solution(s):
    number_list = list(map(int, list(s.split())))
    answer = str(min(number_list)) + ' ' + str(max(number_list))
    return answer