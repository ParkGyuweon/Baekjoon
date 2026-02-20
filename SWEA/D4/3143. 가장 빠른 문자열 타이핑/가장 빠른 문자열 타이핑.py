T = int(input())

for t in range(1, T + 1):
    A, B = input().split()
    if B in A:
        cnt = A.count(B)
    else:
        cnt = 0
    print(f'#{t} {len(A) - (cnt * len(B)) + cnt}')
