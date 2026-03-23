Y, M = map(int, input().split())
if Y < 1:
    year = 0
    month = M * 15
elif Y < 2:
    year = 1 * 15
    month = M * 9
else:
    year =  15 + 9 + (Y - 2) * 4
    month = M * 4
print(year + month // 12, month % 12)