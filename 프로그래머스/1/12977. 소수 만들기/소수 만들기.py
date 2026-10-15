def solution(nums):
    answer = 0
    for num1 in range(len(nums) - 2):
        for num2 in range(num1 + 1, len(nums) - 1):
            for num3 in range(num2 + 1, len(nums)):
                cur_num = nums[num1] + nums[num2] + nums[num3]
                for div in range(2, int(cur_num ** 0.5) + 1):
                    if cur_num % div == 0:
                        break
                else:
                    answer += 1
    return answer