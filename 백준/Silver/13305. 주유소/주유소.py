N = int(input())
distance = list(map(int, input().split()))
fee = list(map(int, input().split()))
idx, cur_money, sum_money = 0, fee[0], 0
while idx < N - 1:
    sum_money = sum_money + (cur_money * distance[idx])
    idx += 1
    if fee[idx] < cur_money:
        cur_money = fee[idx]

print(sum_money)