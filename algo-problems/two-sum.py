# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
# O(n) solution:
def twoSum(nums, target):
    dict = {}

    for i, curr in enumerate(nums):
        n = target - curr
        if n not in dict:
            dict[curr] = i
        else:
            return [dict[n], i]

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))

