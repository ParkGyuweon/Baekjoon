def solution(a, b, n):
    receive_cola = 0
    empty_cola = n
    while empty_cola >= a:
        empty_cola -= a
        empty_cola += b
        receive_cola += b
    return receive_cola