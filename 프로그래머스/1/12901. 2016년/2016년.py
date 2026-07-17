def solution(a, b):
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    for month in range(1, a):
        day += days[month - 1]
    day += b
    answer = week[(day - 1) % 7]
    return answer