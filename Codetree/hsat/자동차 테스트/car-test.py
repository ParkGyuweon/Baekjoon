N, Q = map(int, input().split())
cars = sorted(list(map(int, input().split())))
cars_dict = {}

for idx in range(len(cars)):
    cars_dict[cars[idx]] = idx

for _ in range(Q):
    cur_middle = int(input())
    if cur_middle in cars_dict:
        print(cars_dict[cur_middle] * (N - 1 - cars_dict[cur_middle]))
    else:
        print(0)