# 조건 : 가장 작은 최솟값을 출력(min)
# 각 팀의 경우의 수 구하기 : 전체를 2로 나눌 경우의 수
# 각 팀의 능력치 구하기 : 모든 순열의 능력치의 합
# 모든 쌍의 능력치 -> 각 조합의 능력치를 비교하면 안됨
# 한 명을 추가할 때마다 각 쌍의 능력치를 다시 계산, 가장 적게 차이나는 사람을 고르는 식?

global result
result = 10E9

ability = []
N = int(input())
for i in range(N):
    ability.append(list(map(int, input().split())))

visited = [False] * N

def back(start, count):
    global result
    if count == N // 2:
        t1 = 0
        t2 = 0
 
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    t1 = t1 + ability[i][j]
                if not visited[j] and not visited[i]:
                    t2 = t2 + ability[i][j]

        result = min(result, abs(t1 - t2))

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            back(i, count + 1)
            visited[i] = False
    return

back(0, 0)
print(int(result))