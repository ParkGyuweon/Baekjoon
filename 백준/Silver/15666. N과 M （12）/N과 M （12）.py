N, M = map(int, input().split())
number = list(sorted(map(int, input().split())))
total_set = set()

def back(current, start):
    if len(current) == M:
        if tuple(current) not in total_set:
            print(' '.join(map(str, current)))
            total_set.add(tuple(current))
        return
    for num in range(start, len(number)):
        back(current + [number[num]], num)

back([], 0)