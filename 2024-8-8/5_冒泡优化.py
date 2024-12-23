nums = [25, 20, 1, 26, 13, 2]
print(nums)
n = len(nums) - 1
for j in range(n):
    # n-j 每次内循环就可以少循环j次
    for i in range(n - j):
        if nums[i] > nums[i + 1]:
            # 交换位置
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    print(nums)
