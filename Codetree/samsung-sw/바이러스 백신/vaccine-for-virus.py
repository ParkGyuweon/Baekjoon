from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

hospital_list = []
total_virus = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
for y in range(N):
    for x in range(N):
        if grid[y][x] == 2:
            hospital_list.append([x, y])
        elif grid[y][x] == 0:
            total_virus += 1
if total_virus == 0:
    print(0)
    exit()
total_candidates = []

def back_track(current, x, M):
    if len(current) == M:
        total_candidates.append(list(current))
        return
    for idx in range(x, len(hospital_list)):
        current.append(hospital_list[idx])
        back_track(current, idx + 1, M)
        current.pop()

back_track([], 0, M)
answer = 10E10
for candidate in total_candidates:
    kill_virus, mul_num = 0, 1
    queue = deque()
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for hospital in candidate:
        queue.append((hospital[0], hospital[1], 0))
        visited[hospital[1]][hospital[0]] = 1

    while queue:
        cur_x, cur_y, cur_time= queue.popleft()
        for add_x, add_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = cur_x + add_x, cur_y + add_y
            if 0 <= new_x < N and 0 <= new_y < N and visited[new_y][new_x] == 0 and grid[new_y][new_x] != 1:
                queue.append((new_x, new_y, cur_time + 1))
                visited[new_y][new_x] = 1
                if grid[new_y][new_x] == 0:
                    kill_virus += 1
                    if kill_virus == total_virus:
                        answer = min(answer, cur_time + 1)
                        break

if answer == 10E10:
    print(-1)
else:
    print(answer)