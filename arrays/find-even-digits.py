# Given an array nums of integers, return how many of them contain an even number of digits.

def findEven(nums):
    numEven = 0
    for num in nums:
        digits = 0
        while num / 10 >= 1:
            num = num / 10
            digits += 1
        digits += 1

        if digits % 2 == 0:
            numEven += 1
    return numEven

nums = [555,901,482,1771]

print(findEven(nums))
