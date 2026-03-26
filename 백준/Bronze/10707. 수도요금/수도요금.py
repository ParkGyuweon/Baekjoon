X_fee = int(input())
Y_default_fee = int(input())
Y_max = int(input())
Y_fee = int(input())
cur_use = int(input())

X_total = cur_use * X_fee
if cur_use > Y_max:
    Y_total = Y_default_fee + (cur_use - Y_max) * Y_fee
else:
    Y_total = Y_default_fee

print(min(X_total, Y_total))