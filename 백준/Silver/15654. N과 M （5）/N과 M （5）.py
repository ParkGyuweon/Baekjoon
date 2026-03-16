N, M = map(int, input().split())
number = list(sorted(map(int, input().split())))

def back(current):
    if len(current) == M:
        print(' '.join(map(str, current)))
        return
    for num in number:
        if num in current:
            continue
        back(current + [num])

back([])