from collections import defaultdict

N = int(input())
like_friends = {}
student_order = []
for _ in range(N ** 2):
    one_line = list(map(int, input().split()))
    student_order.append(one_line[0])
    like_friends[one_line[0]] = one_line[1:]
    
grid = [[0 for _ in range(N)] for _ in range(N)]
for student in student_order:
    like_dict = [[-1 for _ in range(N)] for _ in range(N)]
    blank_dict = [[-1 for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if grid[y][x] == 0:
                cur_like = 0
                cur_blank = 0
                for add_x, add_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_x, new_y = x + add_x, y + add_y
                    if 0 <= new_x < N and 0 <= new_y < N:
                        if grid[new_y][new_x] in like_friends[student]:
                            cur_like += 1
                        elif grid[new_y][new_x] == 0:
                            cur_blank += 1
                like_dict[y][x] = cur_like
                blank_dict[y][x] = cur_blank

    cand_num, blank_num, cand_x, cand_y = 0, 0, N - 1, N - 1
    for y in range(N):
        for x in range(N):
            if like_dict[y][x] > cand_num:
                cand_num = like_dict[y][x]
                blank_num = blank_dict[y][x]
                cand_x, cand_y = x, y
            elif like_dict[y][x] == cand_num and blank_dict[y][x] > blank_num:
                blank_num = blank_dict[y][x]
                cand_x, cand_y = x, y
            elif like_dict[y][x] == cand_num and blank_dict[y][x] == blank_num and y < cand_y:
                cand_x, cand_y = x, y
            elif like_dict[y][x] == cand_num and blank_dict[y][x] ==  blank_num and y == cand_y and x < cand_x:
                cand_x, cand_y = x, y

    grid[cand_y][cand_x] = student

answer = 0
score = [0, 1, 10, 100, 1000]
for y in range(N):
    for x in range(N):
        cur_like = 0
        for add_x, add_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + add_x, y + add_y
            if 0 <= new_x < N and 0 <= new_y < N:
                if grid[new_y][new_x] in like_friends[grid[y][x]]:
                    cur_like += 1
        answer += score[cur_like]

print(answer)