result = []

for i in range(4):
    x11, y11, x12, y12, x21, y21, x22, y22 = map(int, input().split())
    L1 = [x11, y11, x12, y12] # 사각형 1
    L2 = [x21, y21, x22, y22] # 사각형 2

    # 쉬운 비교를 위해 더 왼쪽에서 시작하는 사각형을 left, 상대적으로 오른쪽에서 시작하는 사각형을 right라고 함.
    if x11 < x21:
        left = L1
        right = L2
    else:
        left = L2
        right = L1

    # 쉬운 비교를 위해 더 위쪽에서 시작하는 사각형을 up, 상대적으로 아래쪽에 있는 사각형을 down이라고 함.
    if y11 > y21:
        up = L1
        down = L2
    else:
        up = L2
        down = L1

    if left[2] == right[0] and left[3] == right[1]: # 첫 번째 사각형의 북동쪽 점과 두 번째 사각형의 남서쪽 점이 겹치는 경우
        result.append('c')
    elif left[2] == right[0] and left[1] == right[3]: # 첫 번째 사각형의 남동쪽 점과 두 번째 사각형의 북서쪽 점이 겹치는 경우
        result.append('c')
    elif left[2] == right[0] and set(range(left[1], left[3] + 1)).intersection(set(range(right[1], right[3] + 1))):
        result.append('b')
    elif up[1] == down[3] and set(range(up[0], up[2] + 1)).intersection(set(range(down[0], down[2] + 1))):
        result.append('b')
    elif not set(range(left[0], left[2] + 1)).intersection(set(range(right[0], right[2] + 1))):
        result.append('d')
    elif not set(range(left[1], left[3] + 1)).intersection(set(range(right[1], right[3] + 1))): # 전혀 상관 없는 두 개의 사각형을 구분
        result.append('d')
    else:
        result.append('a')

print('\n'.join(result))