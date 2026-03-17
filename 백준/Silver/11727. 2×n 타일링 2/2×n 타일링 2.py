N = int(input())
nemo = [('1', 1), ('22', 2), ('3', 2)]
memo = {}

def paper(cur_width, num):
    global paper_num
    if (num - cur_width) in memo:
        paper_num += memo[(num - cur_width)]
        return
    if cur_width == num:
        paper_num += 1
        return
    if cur_width > num:
        return
    for item, width in nemo:
        paper(cur_width + width, num)

for num in range(1, N + 1):
    paper_num = 0
    paper(0, num)
    memo[num] = paper_num

print(memo[N] % 10007)