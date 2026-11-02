N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
answer = 0
for y in range(N - 2):
    for x in range(N - 2):
        start_x, start_y = x, y
        cur_coin = 0
        for cur_x in range(3):
            for cur_y in range(3):
                if grid[start_y + cur_y][start_x + cur_x] == 1:
                    cur_coin += 1
        answer = max(answer, cur_coin)

print(answer)