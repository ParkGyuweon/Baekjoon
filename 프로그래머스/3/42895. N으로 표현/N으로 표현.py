def solution(N, number):
    cases = [set() for _ in range(9)]
    cases[0].add(0)
    cases[1].add(N)
    if number == N:
        return 1
    total_set = cases[0] | cases[1]
    for cur_use in range(2, 9):
        cases[cur_use].add(int(str(N) * cur_use))
        for first in range(1, int(cur_use // 2) + 1):
            second = cur_use - first
            for fir_num in cases[first]:
                for sec_num in cases[second]:
                    cases[cur_use].add(fir_num + sec_num)
                    cases[cur_use].add(fir_num - sec_num)
                    cases[cur_use].add(sec_num - fir_num)
                    cases[cur_use].add(fir_num * sec_num)
                    if sec_num != 0:
                        cases[cur_use].add(fir_num // sec_num)
                    if fir_num != 0:
                        cases[cur_use].add(sec_num // fir_num)
            if number in cases[cur_use]:
                return cur_use
            
        cases[cur_use] = cases[cur_use] - total_set
        total_set = total_set | cases[cur_use]
    return -1