T = int(input())

for i in range(T):
    L = list(map(int, input().split()))
    answer = False
    same_val = True
    num = L.index(min(L))
    L_sort = sorted(L)
    if L_sort[1] == L_sort[2]:
        answer = True
    for j in range(2):
        if L[j] != L[j + 1]:
            same_val = False
    if not answer :
        print(-1, -1, -1)
    else:
        if same_val:
            print(L[0], L[0], L[0])
        else:
            if L[0] == L[2]:
                print(L_sort[2], min(L), min(L))
            elif L[1] == L[2]:
                print(min(L), min(L), L_sort[2])
            else:
                print(min(L), L_sort[2], min(L))