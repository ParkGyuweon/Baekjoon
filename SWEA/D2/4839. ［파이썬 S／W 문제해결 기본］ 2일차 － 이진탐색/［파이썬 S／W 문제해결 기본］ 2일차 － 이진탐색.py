T = int(input())
for t in range(1, T + 1):
    P, A, B = map(int, input().split())
    start_A, end_A, start_B, end_B = 1, P, 1, P
    A_check, B_check = False, False
    
    while start_A <= end_A and start_B <= end_B:
        middle_A = (start_A + end_A) // 2
        middle_B = (start_B + end_B) // 2
        if middle_A == A and middle_B == B:
            A_check, B_check = True, True
            break
        elif middle_A == A:
            A_check = True
            break
        elif middle_B == B:
            B_check = True
            break
        if A < middle_A:
            end_A = middle_A
        elif A > middle_A:
            start_A = middle_A
        if B < middle_B:
            end_B = middle_B
        elif B > middle_B:
            start_B = middle_B
        
    if A_check and B_check:
        print(f'#{t} 0')
    elif A_check:
        print(f'#{t} A')
    elif B_check:
        print(f'#{t} B')
            