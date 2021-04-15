# Given integer array nums, return the third maximum number in this array.
# If the third maximum does not exist, return the maximum number.

def thirdMax(nums):
    first, second, third = 0,0,0
    firstSet, secondSet, thirdSet = False, False, False

    for i in range(len(nums)):
        if nums[i] >= first or not firstSet:
            if nums[i] != first:
                if firstSet:
                    if secondSet:
                        third = second
                        thirdSet = True
                    second = first
                    secondSet = True

                first = nums[i]
                firstSet = True
        elif nums[i] >= second or not secondSet:
            if nums[i] != second:
                if secondSet:
                    third = second
                    thirdSet = True

                second = nums[i]
                secondSet = True
        elif nums[i] > third or not thirdSet:
            third = nums[i]
            thirdSet = True

    if thirdSet:
        return third
    return first

nums = [1,-2147483648,2]
nums2 = [5,2,2]

print(thirdMax(nums))
print(thirdMax(nums2))
