T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A_index = 0
    B_index = 0
    while B_index != M and A_index != N:
        if A[A_index] == B[B_index]:
            A_index +=1
            B_index +=1
        else:
            A_index += 1

    if B_index == M:
        print(f'#{t + 1} YES')
    else:
        print(f'#{t + 1} NO')