def solution(triangle):
    for height in range(1, len(triangle)):
        for idx in range(len(triangle[height])):
            left, right = idx - 1, idx + 1
            if not (0 <= left):
                triangle[height][idx] = triangle[height - 1][idx] + triangle[height][idx]
            elif not (right < len(triangle[height])):
                triangle[height][idx] = triangle[height - 1][idx - 1] + triangle[height][idx]
            else:
                triangle[height][idx] = max(triangle[height - 1][idx - 1], triangle[height - 1][idx]) + triangle[height][idx]
    return max(triangle[-1])