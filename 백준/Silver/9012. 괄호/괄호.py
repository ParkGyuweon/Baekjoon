N = int(input())
L = []
for i in range(N):
    L.append(list(input()))
    
for i in range(N):
    temp = True
    L_check = []
    for j in range(len(L[i])):
        if len(L_check) == 0 and L[i][j] == ')':
            print("NO")
            temp = False
            break
        elif L[i][j] == ')':
            del L_check[-1]
        else:
            L_check.append('(')
    if not L_check and temp == True:
        print("YES")
    if L_check:
        print("NO")