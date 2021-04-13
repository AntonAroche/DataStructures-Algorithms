# Given a binary array nums, return the maximum number of consecutive 1's in the array.

def findMaxConsecutiveOnes(nums):
    currMax = 0
    counter = 0

    for num in nums:
        if num == 0:
            counter = 0
        else:
            counter += 1

        if counter > currMax:
            currMax = counter

    return currMax

arr = [1,1,0,1,1,1,0,1,0,1,1,1,1,0]

print(findMaxConsecutiveOnes(arr))
