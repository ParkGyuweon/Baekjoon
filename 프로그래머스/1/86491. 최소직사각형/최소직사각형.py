def solution(sizes):
    width, height = 0, 0
    for size in sizes:
        width = max(max(size), width)
        height = max(min(size), height)
    return width * height