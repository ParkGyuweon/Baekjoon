ISBN = list(input())
sum_val = 0

for i in range(12):
    if ISBN[i].isnumeric():
       if i % 2 == 0:
           sum_val = sum_val + int(ISBN[i])
       else:
           sum_val = sum_val + int(ISBN[i]) * 3
    else:
        if i % 2 == 0:
            weight = 1
        else:
            weight = 3
for i in range(10):
    if ((10 - (sum_val + i * weight) % 10)) % 10 == int(ISBN[-1]):
        print(i)
        break
