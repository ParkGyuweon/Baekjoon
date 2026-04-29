def solution(n, left, right):
    # 숫자 채우기
    grid = []
    for idx in range(left, right + 1):
        grid.append(max(idx % n, idx // n) + 1)
        
    return grid