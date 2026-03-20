from collections import deque
N, M = map(int, input().split())
grid = [n for n in range(101)]
visited_grid = [0] * 101

for _ in range(N):
    start, end = map(int, input().split())
    grid[start] = end
for _ in range(M):
    start, end = map(int, input().split())
    grid[start] = end

start_position = 1
min_val = 10E10

def dice_bfs():
    stack = deque([(start_position, 0)])
    while stack:
        cur_position, cur_dice = stack.popleft()
        for number in (1, 2, 3, 4, 5, 6):
            if cur_position + number <= 100:
                if cur_position + number == 100:
                    print(cur_dice + 1)
                    exit()
                elif cur_position + number < 100 and visited_grid[cur_position + number] == 0:
                    stack.append((grid[cur_position + number], cur_dice + 1))
                    visited_grid[cur_position + number] = 1

dice_bfs()