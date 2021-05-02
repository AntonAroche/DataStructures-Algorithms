# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.

def findDisappearedNumbers(nums):
    s = set(nums)
    vals = []

    for n in range(1, len(nums) + 1):
        if n not in s:
            vals.append(n)

    return vals

nums = [4,3,2,7,8,2,3,1]

print(findDisappearedNumbers(nums))
