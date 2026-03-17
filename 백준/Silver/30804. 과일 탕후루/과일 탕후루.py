from collections import defaultdict

N = int(input())
fruits = list(map(int, input().split()))
fruits_dict = defaultdict(int)

max_val, left, right = 0, 0, 0
while left <= right and right < N:
    fruits_dict[fruits[right]] += 1

    if len(fruits_dict) >= 3:
        while left < N:
            fruits_dict[fruits[left]] -= 1
            if fruits_dict[fruits[left]] == 0:
                fruits_dict.pop(fruits[left])
                left += 1
                break
            left += 1

    max_val = max(max_val, right - left + 1)
    right += 1
print(max_val)