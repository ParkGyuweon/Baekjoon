T = int(input())

def queens(idx, cross_line):
    global case_num
    if idx == N:
        case_num += 1
        return

    for x in range(N):
        if not x_list[x]:
            for item in cross_line:
                if abs((item[0] - x) / (item[1] - idx)) == 1:
                    break
            else:
                x_list[x] = True
                cross_line.append((x, idx))
                queens(idx + 1, cross_line)
                x_list[x] = False
                cross_line.pop()



for t in range(1, T + 1):
    N = int(input())
    x_list = [False] * N
    case_num = 0
    queens(0, [])

    print(f'#{t} {case_num}')