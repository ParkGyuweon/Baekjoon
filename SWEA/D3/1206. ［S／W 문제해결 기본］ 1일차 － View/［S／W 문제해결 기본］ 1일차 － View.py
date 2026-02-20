for i in range(10):
    N = int(input())
    building  = list(map(int, input().split()))
    good = 0
    
    # 방법 1 ) 주변 4개의 건물 중 현재 건물이 가장 높은 지 확인 후, 주변 건물 중 가장 높은 건물과의 차이를 구해서 더함
#    for j in range(2, N - 1):
#        if building[j - 1] < building[j] and building[j - 2] < building[j] and building[j + 1] < building[j] and building[j + 2] < building[j]:
#                good = good + (building[j] - max(building[j - 2], building[j - 1], building[j + 2], building[j + 1]))
                
    # 방법 2 ) max 안 쓰기 -> 하나하나 비교해서 최댓값 교환
    for j in range(2, N - 1):
        max_val = 0
        if building[j - 1] < building[j] and building[j - 2] < building[j] and building[j + 1] < building[j] and building[j + 2] < building[j]:
            if building[j - 2] > max_val:
                max_val = building[j - 2]
            if building[j - 1] > max_val:
                max_val = building[j - 1]
            if building[j + 2] > max_val:
                max_val = building[j + 2]
            if building[j + 1] > max_val:
                max_val = building[j + 1] 
            good = good + (building[j] - max_val)
            
    print(f'#{i + 1} {good}')