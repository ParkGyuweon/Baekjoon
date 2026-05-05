def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        number_list = [0] * (n + 1)
        number_list[1] = 1
        number_list[2] = 2
        for idx in range(3, len(number_list)):
            number_list[idx] = (number_list[idx - 1] + number_list[idx - 2]) % 1000000007
        return number_list[n]