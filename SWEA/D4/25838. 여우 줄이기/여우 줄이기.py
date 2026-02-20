TC = int(input())

for i in range(TC):
    N = int(input())
    string = input()
    L = []
    for j in range(N):
        if string[j] == 'x' and len(L) >= 2:
            if L[-1] == 'o' and L[-2] == 'f':
                L.pop()
                L.pop()
                continue
        L.append(string[j])
       
    print(len(L))
                