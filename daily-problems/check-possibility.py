# Given an array nums with n integers, your task is to check if it could become non-decreasing
# by modifying at most one element.
#
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds
# for every i (0-based) such that (0 <= i <= n - 2).

def checkPossibility(nums):
    foundFlag = False

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            if foundFlag:
                return False
            foundFlag = True

            if i == 1 or i == len(nums) - 1:
                continue
            elif nums[i - 2] <= nums[i]:
                continue
            elif nums[i - 1] > nums[i + 1]:
                return False
    return True

nums = [5,7,1,8]
nums2 = [3,4,2,3]
nums3 = [-1,4,2,3]

print(checkPossibility(nums), "expected", True)
print(checkPossibility(nums2), "expected", False)
print(checkPossibility(nums3), "expected", True)

