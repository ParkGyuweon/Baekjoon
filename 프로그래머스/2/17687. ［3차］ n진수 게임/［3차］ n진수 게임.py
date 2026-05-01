def solution(n, t, m, p):
    answer = ''
    total_list = ''
    conversion = {0 : '0', 1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 
                 6 : '6', 7 : '7', 8 : '8', 9 : '9', 10 : 'A', 11 : 'B',
                 12 : 'C', 13 : 'D', 14 : 'E', 15 : 'F'}
    for turn in range(t * m):
        cur_number = ''
        number = turn
        if number == 0:
            cur_number = '0'
        else:
            while number != 0:
                cur_number += conversion[number % n]
                number = number // n
        total_list += cur_number[::-1]
        if len(total_list) >= t * m:
            break
    for char_idx in range(len(total_list)):
        if (char_idx % m) + 1 == p:
            answer += total_list[char_idx]
        if len(answer) == t:
            break
    return answer