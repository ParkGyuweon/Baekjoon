N, M = map(int, input().split())
number = list(sorted(map(int, input().split())))
total_set = set()

def back(current, idx_list):
    if len(current) == M:
        if tuple(current) not in total_set:
            print(' '.join(map(str, current)))
            total_set.add(tuple(current))
        return
    for num in range(len(number)):
        if num in idx_list:
            continue
        back(current + [number[num]], idx_list + [num])

back([], [])