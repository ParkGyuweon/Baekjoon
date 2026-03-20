import sys
from collections import defaultdict
import heapq
T = int(input())
input = sys.stdin.readline

for t in range(1, T + 1):
    K = int(input().strip())
    total_number = defaultdict(int)
    number_max = []
    number_min = []
    delete_num = 0
    insert_num = 0

    for _ in range(K):
        command, num = input().split()
        if command == 'I':
            insert_num += 1
            total_number[int(num)] += 1
            heapq.heappush(number_min, int(num))
            heapq.heappush(number_max, int(num) * -1)
        elif command == 'D' and insert_num > delete_num:
            if num == '1':
                while True:
                    cur_val = heapq.heappop(number_max) * -1
                    if total_number[cur_val] > 0:
                        total_number[cur_val] -=1
                        break
            else:
                while True:
                    cur_val = heapq.heappop(number_min)
                    if total_number[cur_val] > 0:
                        total_number[cur_val] -= 1
                        break

            delete_num += 1
    if insert_num == delete_num:
        print('EMPTY')
    else:
        while True:
            cur_max = heapq.heappop(number_max) * -1
            if total_number[cur_max] > 0:
                break
        while True:
            cur_min = heapq.heappop(number_min)
            if total_number[cur_min] > 0:
                break
        print(cur_max, cur_min)