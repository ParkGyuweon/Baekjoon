def solution(numbers, hand):
    answer = ''
    number_dict = {1 : (0, 0), 2: (1, 0), 3: (2, 0), 4: (0, 1), 5: (1, 1), 6: (2, 1), 7: (0, 2), 8: (1, 2), 9: (2, 2), '*' : (0, 3), 0: (1, 3), '#': (2, 3)}
    cur_left_x, cur_left_y, cur_right_x, cur_right_y = 0, 3, 2, 3
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            cur_left_x, cur_left_y = number_dict[number]
        elif number in [3, 6, 9]:
            answer += 'R'
            cur_right_x, cur_right_y = number_dict[number]
        else:
            next_x, next_y = number_dict[number]
            if abs(cur_left_x - next_x) + abs(cur_left_y - next_y) < abs(cur_right_x - next_x) + abs(cur_right_y - next_y):
                answer += 'L'
                cur_left_x, cur_left_y = next_x, next_y
            elif abs(cur_left_x - next_x) + abs(cur_left_y - next_y) > abs(cur_right_x - next_x) + abs(cur_right_y - next_y):
                answer += 'R'
                cur_right_x, cur_right_y = next_x, next_y
            else:
                if hand == 'left':
                    answer += 'L'
                    cur_left_x, cur_left_y = next_x, next_y
                else:
                    answer += 'R'
                    cur_right_x, cur_right_y = next_x, next_y
    return answer