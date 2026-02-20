for t in range(1, 11):
    N = int(input())  # 입력 데이터에서 테스트 케이스 번호 받기
    ladder = [list(map(int, input().split())) for _ in range(100)]  # 행렬의 값을 다차원 리스트로 입력 받기
    start_list = []
    result = 0

    start = 0
    current_ladder = ladder[0]
    while 1 in current_ladder:
        start_list.append(ladder[0].index(1, start, 100))
        start = start_list[-1] + 1
        current_ladder = ladder[0][start:]

    # 배열에 저장된 순서대로 사다리 타기 시작
    for item in start_list:
        # 시작 위치가 저장된 배열을 순회하며 위치 저장
        dx, dy = [0, -1, 1], [1, 0, 0]
        cur_x, cur_y, direction = item, 0, 0

        while cur_y <= 99:
            if direction == 0:
                if cur_x >= 1 and ladder[cur_y][cur_x - 1] == 1:
                    direction = 1
                elif cur_x <= 98 and ladder[cur_y][cur_x + 1] == 1:
                    direction = 2
            elif direction == 1 and cur_y < 99 and ladder[cur_y + 1][cur_x] == 1:
                direction = 0
            elif direction == 2 and cur_y < 99 and ladder[cur_y + 1][cur_x] == 1:
                direction = 0
            cur_x, cur_y = cur_x + dx[direction], cur_y + dy[direction]

        if ladder[99][cur_x] == 2:
            print(f'#{t} {item}')
            break