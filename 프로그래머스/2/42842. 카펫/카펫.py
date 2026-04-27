def solution(brown, yellow):
    answer = []
    total_grid = brown + yellow
    for height in range(1, int(total_grid ** (1/2)) + 1):
        if total_grid / height == total_grid // height:
            width = total_grid // height
        else:
            continue
        if width * 2 + height * 2 - 4 == brown and width >= height:
            answer = [width, height]
            break
        else:
            continue
            
    return answer