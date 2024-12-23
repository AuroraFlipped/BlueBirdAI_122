nums = [25, 20, 1, 26, 13, 2]
print(nums)
n = len(nums) - 1
for j in range(n):
    for i in range(n):
        if nums[i] > nums[i + 1]:
            # 交换位置
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
print(nums)
