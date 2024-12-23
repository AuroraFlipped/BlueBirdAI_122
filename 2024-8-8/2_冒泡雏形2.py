# a,b = 3,4
nums = [25, 20, 1, 26, 13, 2]
print(nums)
# 比较大小交换位置把大的那个放后面
# if nums[0] > nums[1]:
#     # 交换位置
#     nums[0], nums[1] = nums[1], nums[0]
# print(nums)
# if nums[1] > nums[2]:
#     # 交换位置
#     nums[1], nums[2] = nums[2], nums[1]
# print(nums)
# if nums[2] > nums[3]:
#     # 交换位置
#     nums[2], nums[3] = nums[3], nums[2]
# print(nums)
# if nums[3] > nums[4]:
#     # 交换位置
#     nums[3], nums[4] = nums[4], nums[3]
# print(nums)
# if nums[4] > nums[5]:
#     # 交换位置
#     nums[4], nums[5] = nums[5], nums[4]
# print(nums)
n = len(nums) - 1
for i in range(0, n):
    if nums[i] > nums[i + 1]:
        # 交换位置
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
print(nums)
