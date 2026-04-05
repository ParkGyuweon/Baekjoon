grid = [list(input()) for _ in range(8)]
answer = 0

for y in range(8):
    for x in range(8):
        if grid[y][x] == 'F' and ((x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1)):
            answer += 1
            
print(answer)