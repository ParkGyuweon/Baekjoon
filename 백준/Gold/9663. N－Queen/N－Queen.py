import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용
N = int(sys.stdin.readline())

count = 0
# 3종류의 visited 배열을 생성
visited_col = [False] * N         # 열 사용 여부
visited_diag1 = [False] * (2*N-1) # / 대각선 사용 여부 (x + y)
visited_diag2 = [False] * (2*N-1) # \ 대각선 사용 여부 (x - y + N-1)

def back(x):
    """ x번째 행에 퀸을 놓는 함수 """
    global count
    
    # 마지막 행까지 퀸을 모두 놓았다면, 경우의 수 1 증가
    if x == N:
        count += 1
        return

    # 현재 x행의 y열에 퀸을 놓을지 시도
    for y in range(N):
        # 현재 위치 (x, y)가 다른 퀸에게 공격받지 않는 위치인지 확인
        if not visited_col[y] and not visited_diag1[x+y] and not visited_diag2[x-y + N-1]:
            # 퀸을 놓았으므로, 해당 위치의 열과 대각선을 방문 처리(True)
            visited_col[y] = True
            visited_diag1[x+y] = True
            visited_diag2[x-y + N-1] = True
            
            # 다음 행으로 재귀 호출
            back(x + 1)
            
            # 재귀 호출이 끝났으면, 현재 놓았던 퀸을 다시 회수 (백트래킹)
            # 방문 표시를 False로 되돌려 놓아야 다른 경우의 수를 탐색할 수 있음
            visited_col[y] = False
            visited_diag1[x+y] = False
            visited_diag2[x-y + N-1] = False

# 0번째 행부터 시작
back(0)
print(count)