T = int(input())
num_dict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
            '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
            'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

conversion_two_to_int = {'3211': '0', '2221': '1', '2122': '2', '1411': '3',
                         '1132': '4', '1231': '5', '1114': '6', '1312': '7',
                         '1213': '8', '3112': '9'}

for t in range(1, T + 1):
    N, M = map(int, input().split())
    total_answer = 0
    grid = [input() for _ in range(N)]
    code_set = set()
    for y in range(N):
        cur_line = ''
        for x in range(M):
            cur_line += num_dict[grid[y][x]]
        while cur_line.count('0') != len(cur_line):
            for idx in range(len(cur_line) - 1, -1, -1):
                if cur_line[idx] == '1':
                    code_ratio = [0] * 4
                    cur_idx = idx
                    while cur_line[cur_idx] == '1':
                        code_ratio[3] += 1
                        cur_idx -= 1
                    while cur_line[cur_idx] == '0':
                        code_ratio[2] += 1
                        cur_idx -= 1
                    while cur_line[cur_idx] == '1':
                        code_ratio[1] += 1
                        cur_idx -= 1
                    while cur_line[cur_idx] == '0':
                        code_ratio[0] += 1
                        cur_idx -= 1
                    cur_ratio = sum(code_ratio) // 7
                    code_set.add(cur_line[idx - 56 * cur_ratio + 1: idx + 1])
                    cur_line = cur_line[: idx - 56 * cur_ratio + 1]
                    break

    for item in code_set:
        cur_code = ''
        code_ratio = len(item) // 56
        for position in range(0, len(item), 7 * code_ratio):
            cur_ratio = [0] * 4
            cur_idx = position
            while item[cur_idx] == '0':
                cur_ratio[0] += 1
                cur_idx += 1
            while item[cur_idx] == '1':
                cur_ratio[1] += 1
                cur_idx += 1
            while item[cur_idx] == '0':
                cur_ratio[2] += 1
                cur_idx += 1
            while cur_idx < len(item) and item[cur_idx] == '1':
                cur_ratio[3] += 1
                cur_idx += 1
            cur_code += conversion_two_to_int[''.join(map(str, [item // code_ratio for item in cur_ratio]))]
        if (3 * (int(cur_code[0]) + int(cur_code[2]) + int(cur_code[4]) + int(cur_code[6]))
                 + int(cur_code[1]) + int(cur_code[3]) + int(cur_code[5]) + int(cur_code[7])) % 10 == 0:
            total_answer += sum(map(int, cur_code))
    print(f'#{t} {total_answer}')