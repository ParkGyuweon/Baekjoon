T = int(input())

def merge(left, right):
    global case_num
    result = [0] * (len(left) + len(right))
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    while l < len(left):
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        result[l + r] = right[r]
        r += 1

    if left[-1] > right[-1]:
        case_num += 1

    return result

def merge_sort(li):
    if len(li) == 1:
        return li

    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]

    left_list = merge_sort(left)
    right_list = merge_sort(right)

    merge_list = merge(left_list, right_list)
    return merge_list

for t in range(1, T + 1):
    N = int(input())
    number_list = list(map(int, input().split()))
    case_num = 0
    number_list = merge_sort(number_list)
    print(f'#{t} {number_list[N // 2]} {case_num}')

