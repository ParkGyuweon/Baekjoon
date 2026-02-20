from collections import deque

for T in range(1, 11):
    t = int(input())
    grid = [list(input()) for _ in range(100)]
    max_pall = 0  # 최대 회문의 길이를 저장하는 변수

    flag = False  # 회문을 찾았는지 여부를 나타내는 변수
    for m in range(100, 0, -1):  # 회문의 길이를 변화시킴
        for y in range(100):  # y축
            for x in range(100 - m + 1):  # 시작점이 될 수 있는 x축 지점
                one_line = deque(grid[y][x:x + m])  # 슬라이싱해서 m 길이의 리스트를 따로 만들음
                while len(one_line) > 1 and one_line.popleft() == one_line.pop():  # 양쪽 끝이 같은지 확인함
                    if len(one_line) <= 1 and m > max_pall:
                        max_pall = m
    if not flag:
        grid = list(zip(*grid))
    for m in range(100, 0, -1):  # 회문의 길이를 변화시킴
        for y in range(100):  # y축
            for x in range(100 - m + 1):  # 시작점이 될 수 있는 x축 지점
                one_line = deque(grid[y][x:x + m])  # 슬라이싱해서 m 길이의 리스트를 따로 만들음
                while len(one_line) > 1 and one_line.popleft() == one_line.pop():  # 양쪽 끝이 같은지 확인함
                    if len(one_line) <= 1 and m > max_pall:
                        max_pall = m
    
    print(f'#{t} {max_pall}')