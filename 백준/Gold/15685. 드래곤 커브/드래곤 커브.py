N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
def dragon(start_x, start_y, cur_dir, generation):
    stack = [cur_dir]
    position = {(start_x, start_y)}
    cur_gene = 0
    cur_x, cur_y = (start_x, start_y)
    cur_position = []
    while cur_gene <= generation:
        cur_dir = stack.pop()
        cur_x, cur_y = (cur_x + direction[cur_dir][0], cur_y + direction[cur_dir][1])
        cur_position.append((cur_dir + 1) % 4)
        if not stack:
            cur_gene += 1
            stack = list(cur_position)

        position.add((cur_x, cur_y))
    return position

total_list = set()
for item in grid:
    start_x, start_y, cur_dir, generation = item
    total_list = total_list | dragon(start_x, start_y, cur_dir, generation)

box = 0
for y in range(100):
    for x in range(100):
        if (x, y) in total_list and (x + 1, y) in total_list and (x, y + 1) in total_list and (x + 1, y + 1) in total_list:
            box += 1
print(box)