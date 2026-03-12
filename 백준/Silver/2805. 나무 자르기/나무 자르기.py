from collections import defaultdict

N, M = map(int, input().split())
height_tree = list(map(int, input().split()))
tree_dict = defaultdict(int)
for tree in height_tree:
    tree_dict[tree] += 1
set_tree = list(sorted(list(set(height_tree)), reverse=True))
left, right = 0, max(height_tree)
result = 0

while left <= right:
    mid = (left + right) // 2
    cur_tree = 0
    for key in set_tree:
        if key <= mid:
            break
        cur_tree += tree_dict[key] * (key - mid)
    if cur_tree >= M:
        left = mid + 1
        result = mid
    else:
        right = mid -1

print(result)