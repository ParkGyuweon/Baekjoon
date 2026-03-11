T = int(input())

def binary_search_while(target, A):
    left_flag, right_flag, total_flag = False, False, True
    left = 0
    right = len(A) - 1

    while left <= right:
        mid = (left + right) // 2

        if A[mid] == target:
            return mid, total_flag

        if target < A[mid]:
            if left_flag == True:
                total_flag = False
            left_flag, right_flag = True, False
            right = mid - 1
        else:
            if right_flag == True:
                total_flag = False
            left_flag, right_flag = False, True
            left = mid + 1

    return -1

for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(sorted(list(map(int, input().split()))))
    B = list(map(int, input().split()))
    num_case = 0

    for num in B:
        result = binary_search_while(num, A)
        if result != -1 and result[1] == True:
            num_case += 1
    print(f'#{t} {num_case}')