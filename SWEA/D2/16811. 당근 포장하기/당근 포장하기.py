from collections import defaultdict
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()
    set_carrot = list(sorted(set(carrot)))
    dict_carrot = defaultdict(int)
    min_val = 10E10
    for i in carrot:
        dict_carrot[i] += 1

    for first in range(0, len(set_carrot) - 2):
        if min_val == 0:
            break
        first_box = []
        for idx in range(first + 1):
            first_box.extend([set_carrot[idx]] * dict_carrot[set_carrot[idx]])
        for second in range(first + 1, len(set_carrot) - 1):
            second_box = []
            third_box = []
            for sec_idx in range(first + 1, second + 1):
                second_box.extend([set_carrot[sec_idx]] * dict_carrot[set_carrot[sec_idx]])
            for idx in range(second + 1, len(set_carrot)):
                third_box.extend([set_carrot[idx]] * dict_carrot[set_carrot[idx]])
            if len(first_box) > N // 2 or len(second_box) > N // 2 or len(third_box) > N // 2:
                continue
            min_val = min(min_val, max(abs(len(first_box) - len(second_box)), abs(len(first_box) - len(third_box)), abs(len(second_box) - len(third_box))))
    if min_val == 10E10:
        print(f'#{t} -1')
    else:
        print(f'#{t} {min_val}')