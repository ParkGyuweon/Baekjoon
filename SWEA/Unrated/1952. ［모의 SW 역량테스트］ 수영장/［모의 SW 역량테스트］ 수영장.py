T = int(input())
def pool_dfs(cur_fee, month):
    global min_fee
    if cur_fee >= min_fee:
        return

    if month >= 12:
        min_fee = min(min_fee, cur_fee)
        return

    if year_plan[month] == 0:
        pool_dfs(cur_fee, month + 1)
    else:
        pool_dfs(cur_fee + month_fee, month + 1)
        pool_dfs(cur_fee + (day_fee * year_plan[month]), month + 1)
        pool_dfs(cur_fee + months_fee, month + 3)

for t in range(1, T + 1):
    day_fee, month_fee, months_fee, year_fee = map(int, input().split())
    min_fee = year_fee
    year_plan = list(map(int, input().split()))
    pool_dfs(0, 0)
    print(f'#{t} {min_fee}')