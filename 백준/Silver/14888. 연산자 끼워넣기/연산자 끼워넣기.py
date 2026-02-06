N = int(input())
num = list(map(int, input().split()))
op_num = list(map(int, input().split()))
op_list = ['+', '-', '*', '//']
op = []
combination = []

for i in range(4): # 전체 operation list
    for j in range(op_num[i]):
        op.append(op_list[i])

op.sort()

com_result = []
visited = [False] * (N - 1)
# 내가 확인할 것 -> 값 위주로 나눔(계산 결과를 리스트에 저장한 후, max와 min 값 도출)
# 맞춰야 하는 조건(중복이 아닐 것)
# 세부적으로 맞춰야 하는 조건(모든 연산자가 들어갈 것, 각기 다른 순서로, 순서가 중복이 아닐 것)
# 이건 백트래킹을 두 번 해야 하는 건가...?

def com(): # 서로 다른 operation 조합을 만드는 코드
    if len(combination) == N - 1:
        com_result.append(list(combination))
        return
    else:
        for i in range(N - 1):
            if i > 0:
                if not visited[i - 1] and op[i - 1] == op[i]:
                    continue
                    
            if not visited[i]:
                combination.append(op[i])
                visited[i] = True
                com()
                combination.pop()
                visited[i] = False
    return

com()
r_L = []
for i in range(len(com_result)):
    result = num[0]
    for j in range(1, N):
        if com_result[i][j - 1] == '+':
            result = result + num[j]
        elif com_result[i][j - 1] == '-':
            result = result - num[j]
        elif com_result[i][j - 1] == '*':
            result = result * num[j]
        else:
            if result < 0 or num[j] < 0:
                result = -1 * (abs(result) // abs(num[j]))
            else:
                result = result // num[j]
    r_L.append(result)

print(max(r_L))
print(min(r_L))