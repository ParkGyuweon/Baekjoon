N, M, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
shark_list = [[] for _ in range(M)]
shark_priority = []
stack = []
direction = {1 : (0, -1), 2 : (0, 1), 3 : (-1, 0), 4 : (1, 0)}
shark_move = 0
shark_smell_list = [{} for _ in range(M)]

for y in range(N):
    for x in range(N): # 상어의 좌표 저장
        if grid[y][x] != 0:
            shark_list[grid[y][x] - 1].append(x)
            shark_list[grid[y][x] - 1].append(y)
            stack.append((x, y, grid[y][x]))
            shark_smell_list[grid[y][x] - 1][(x, y)] = 0
stack.sort(key=lambda x:x[2])

line = list(map(int, input().split()))
for i in range(M): # 상어의 처음 방향 저장
    shark_list[i].append(line[i])

for i in range(M): # 상어의 방향에 따른 우선 순위 저장
    current_shark = {}
    for j in range(4):
        current_shark[j + 1] = list(map(int, input().split()))
    shark_priority.append(current_shark)

# 상어마다 이동 시간을 한번에 관리
# 특정 상어가 이동할 때, 새로운 칸에 냄새를 남기기 전에
# 해당 상어의 냄새가 있는 곳의 시간을 확인 (모두 1씩 증가)
# 증가시키는 과정에서 k가 된 걸 확인하면 0으로 함
# 한 상어가 이동하는 방향은 하나로 정해져 있음 -> 상어 시간 따로 관리 가능
# 0이 되면 grid에서도 0으로 바꿔줘야 함

def bfs(grid, stack):
    global shark_move
    candidate = {}
    temp_stack = []
    while stack:
        cur_x, cur_y, shark_num = stack.pop(0)
        cur_priority = shark_priority[shark_num - 1][shark_list[shark_num - 1][2]]
        for cur_dir in cur_priority:
            x, y = direction[cur_dir]
            new_x, new_y = cur_x + x, cur_y + y
            if 0 <= new_x < N and 0 <= new_y < N and grid[new_y][new_x] == 0:
                if (new_x, new_y) not in candidate:
                    candidate[(new_x, new_y)] = shark_num # 아무 냄새도 없는 칸이 있는 경우
                    shark_list[shark_num - 1][2] = cur_dir
                    temp_stack.append((new_x, new_y, shark_num))
                    shark_smell_list[shark_num - 1][(new_x, new_y)] = -1 # 새롭게 냄새가 추가된 것이므로 넣음
                break
        else:
            for cur_dir in cur_priority:
                x, y = direction[cur_dir]
                new_x, new_y = cur_x + x, cur_y + y
                if 0 <= new_x < N and 0 <= new_y < N and grid[new_y][new_x] == shark_num:
                    if (new_x, new_y) not in candidate:
                        candidate[(new_x, new_y)] = shark_num
                        shark_list[shark_num - 1][2] = cur_dir
                        temp_stack.append((new_x, new_y, shark_num))
                        shark_smell_list[shark_num - 1][(new_x, new_y)] = -1 # 다시 냄새를 뿌렸으므로 -1로 초기화
                    break
            else:
                if (cur_x, cur_y) not in candidate:
                    candidate[(cur_x, cur_y)] = shark_num  # 아무 냄새도 없는 칸이 없는 경우
                    shark_smell_list[shark_num - 1][(cur_x, cur_y)] = -1
                    temp_stack.append((cur_x, cur_y, shark_num))

        if not stack:
            shark_move += 1
            if len(candidate) == 1:
                return shark_move

            stack = temp_stack
            temp_stack = []

            for shark in range(M):
                for key in list(shark_smell_list[shark].keys()):
                    if shark_smell_list[shark][key] + 1 == K:
                        del shark_smell_list[shark][key]
                        grid[key[1]][key[0]] = 0
                    else:
                        shark_smell_list[shark][key] += 1

            for key, value in candidate.items():
                grid[key[1]][key[0]] = value
            candidate = {}

            if shark_move >= 1000:
                return -1
print(bfs(grid, stack))
# grid는 냄새 정보를 저장하는 곳
# candidate는 한 turn에서의 상어들의 위치를 저장하는 곳
# temp_stack은 나중에 stack으로 쓸 요소
# stack을 중간에 갱신하지 않고 turn 단위로 갱신하므로 stack이 비면 한 turn이 끝났다는 것
# 처음에 stack을 상어 순서대로 정렬했으므로 들어올 때도 작은 상어 순서대로 들어옴