T = int(input())


def lomuto_partition(left, right):
    pivot = number_list[right]

    i = left - 1
    for j in range(left, right):
        if number_list[j] <= pivot:
            i += 1
            number_list[i], number_list[j] = number_list[j], number_list[i]

    number_list[i + 1], number_list[right] = number_list[right], number_list[i + 1]
    return i + 1


def quick_sort(left, right):
    if left < right:
        pivot = lomuto_partition(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)

for t in range(1, T + 1):
    N = int(input())
    number_list = list(map(int, input().split()))
    quick_sort(0, len(number_list) - 1)
    print(f'#{t} {number_list[N // 2]}')