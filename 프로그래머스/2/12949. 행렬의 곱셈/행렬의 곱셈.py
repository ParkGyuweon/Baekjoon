def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for y in range(len(arr1)):
        for x2 in range(len(arr2[0])):
            for x in range(len(arr1[y])):
                answer[y][x2] += arr1[y][x] * arr2[x][x2]
    return answer
