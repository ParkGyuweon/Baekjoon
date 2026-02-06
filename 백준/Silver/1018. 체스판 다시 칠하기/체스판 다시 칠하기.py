N, M = map(int, input().split())
L_total = []

L_total_black = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

L_total_white = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

for i in range(N):
    L = list(input().strip())
    L_total.append(L)

L_count = []

'''
def change_color(A, B, count):
    if (A == B) and (A == 'W'):
        B = 'B'
        count = count + 1
    if (A == B) and (A == 'B'):
        B = 'W'
        count = count + 1
    
    return count
'''

wid = 0
hei = 0

for i in range((N - 7) * (M - 7)):
    count_black = 0
    count_white = 0
    for n in range(8):
        for m in range(8):
             if (L_total[n + hei][m + wid] != L_total_black[n][m]):
                    count_black = count_black + 1
             if (L_total[n + hei][m + wid] != L_total_white[n][m]):
                    count_white = count_white + 1
    L_count.append(count_black)
    L_count.append(count_white)
    
    '''
    if (L_total2[wid + (hei * 8)] == 'W'):
        for j in range(7):
            for k in range(7):
                count = change_color(L_total2[k], L_total2[k + 1], count)
                count = change_color(L_total2[j * 8 + k], L_total2[(j + 1) * 8 + k], count)
        count = change_color(L_total2[((hei + 7) * 8) + 6], L_total2[((hei + 7) * 8) + 7], count)
        L_count.append(count)
        L_total2 = []
    
    if (L_total3[wid + (hei * 8)] == 'W'):
        L_total3[wid + (hei * 8)] = 'B'
        count = count + 1
        for j in range(7):
            for k in range(7):
                count = change_color(L_total3[k], L_total3[k + 1], count)
                count = change_color(L_total3[j * 8 + k], L_total3[(j + 1) * 8 + k], count)
        count = change_color(L_total3[((hei + 7) * 8) + 6], L_total3[((hei + 7) * 8) + 7], count)
        L_count.append(count)
        L_total3 = []
        
    if (L_total2[wid + (hei * 8)] == 'B'):
        for j in range(7):
            for k in range(7):
                count = change_color(L_total2[k], L_total2[k + 1], count)
                count = change_color(L_total2[j * 8 + k], L_total2[(j + 1) * 8 + k], count)
        count = change_color(L_total2[((hei + 7) * 8) + 6], L_total2[((hei + 7) * 8) + 7], count)
        L_count.append(count)
        L_total2 = []

    if (L_total3[wid + (hei * 8)] == 'B'):
        L_total3[wid + (hei * 8)] = 'W'
        count = count + 1
        for j in range(7):
            for k in range(7):
                count = change_color(L_total3[k], L_total3[k + 1], count)
                count = change_color(L_total3[j * 8 + k], L_total3[(j + 1) * 8 + k], count)
        count = change_color(L_total3[((hei + 7) * 8) + 6], L_total3[((hei + 7) * 8) + 7], count)
        L_count.append(count)
        L_total3 = []
    '''
    
    if (wid < M - 8):
        wid = wid + 1
    else:
        hei = hei + 1
        wid = 0

print(min(L_count))