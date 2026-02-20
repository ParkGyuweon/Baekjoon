T = int(input())
for t in range(1, T + 1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        if 2 in miro[i]:
            start = (miro[i].index(2), i)
        if 3 in miro[i]:
            end = (miro[i].index(3), i)

    x, y = start
    visited, stack, direction = [(x, y)], [(x, y)], [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while True:
        cur_x, cur_y = stack.pop()
        for i in range(4):
            new_x, new_y = cur_x + direction[i][0],cur_y + direction[i][1]
            if (0 <= new_x < N and 0 <= new_y < N) and (new_x, new_y) not in visited and miro[new_y][new_x] in (0, 3):
                stack.append((new_x, new_y))
                visited.append((new_x, new_y))

        if cur_x == end[0] and cur_y == end[1]:
            print(f'#{t} 1')
            break

        if not stack:
            print(f'#{t} 0')
            break