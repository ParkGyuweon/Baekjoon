T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    members = [set([person]) for person in range(0, N + 1)]
    existed = [i for i in range(0, N + 1)]
    number_list = list(map(int, input().split()))

    for paper in range(0, M * 2, 2):
        min_val, max_val = min(number_list[paper], number_list[paper + 1]), max(number_list[paper], number_list[paper + 1])
        group_min, group_max = existed[min_val], existed[max_val]
        if group_min != group_max:
            for member in members[group_max]:
                existed[member] = group_min
            members[group_min] = members[group_min] | members[group_max]
            members[group_max] = 0
    print(f'#{t} {N - members.count(0)}')