def solution(s):
    cnt = 0
    zero_cnt = 0
    result = s
    while result != '1':
        zero_cnt += result.count('0')
        result = bin(result.count('1'))[2:]
        cnt += 1
    answer = [cnt, zero_cnt]
    return answer