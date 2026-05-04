def solution(land):
    for idx in range(1, len(land)):
        land[idx][1] += max(land[idx - 1][0], land[idx - 1][2], land[idx - 1][3])
        land[idx][0] += max(land[idx - 1][1], land[idx - 1][2], land[idx - 1][3])
        land[idx][2] += max(land[idx - 1][0], land[idx - 1][1], land[idx - 1][3])
        land[idx][3] += max(land[idx - 1][0], land[idx - 1][2], land[idx - 1][1])
    return max(land[-1])