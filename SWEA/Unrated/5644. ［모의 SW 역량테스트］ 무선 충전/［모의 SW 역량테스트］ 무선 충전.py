T = int(input())
dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]

for t in range(1, T + 1):
    M, A = map(int, input().split())
    A_move = [0] + list(map(int, input().split()))
    B_move = [0] + list(map(int, input().split()))
    A_x, A_y, B_x, B_y = 0, 0, 9, 9
    
    battery_list = []
    for _ in range(A):
        X, Y, C, P = map(int, input().split())
        battery_list.append((X - 1, Y - 1, C, P))
        
    battery_list.sort(key=lambda x: -x[3])

    grid = [[[0 for _ in range(A)] for _ in range(10)] for _ in range(10)]
    for idx in range(A):
        battery = battery_list[idx]
        for y in range(10):
            for x in range(10):
                if abs(x - battery[0]) + abs(y - battery[1]) <= battery[2]:
                    grid[y][x][idx] = battery[3]

    total_charge = 0
    for time in range(M + 1):
        A_x += dx[A_move[time]]
        A_y += dy[A_move[time]]
        B_x += dx[B_move[time]]
        B_y += dy[B_move[time]]

        max_p = 0
        for a_bc in range(A):
            for b_bc in range(A):
                charge_a = grid[A_y][A_x][a_bc]
                charge_b = grid[B_y][B_x][b_bc]
                
                if a_bc == b_bc and charge_a > 0:
                    current_p = charge_a
                else:
                    current_p = charge_a + charge_b
                
                if current_p > max_p:
                    max_p = current_p
                    
        total_charge += max_p

    print(f'#{t} {total_charge}')