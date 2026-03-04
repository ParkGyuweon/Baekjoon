T = int(input())
for t in range(1,  T + 1):
    number = float(input())
    cur_2 = []
    turn = 0
    while number != 0:
        turn += 1
        cur_2.append(int(number >= 0.5 ** turn))
        if number >= 0.5 ** turn:
            number = number - (0.5) ** turn
        if len(cur_2) >= 13:
            print(f'#{t} overflow')
            break
    else:
        print(f'#{t} {"".join(map(str, cur_2))}')