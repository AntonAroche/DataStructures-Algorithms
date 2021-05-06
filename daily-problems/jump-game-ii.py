# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# You can assume that you can always reach the last index.

def jump(nums):
    jumpTotal = 0
    finished = False
    currIdx = 0

    while not finished:
        if currIdx == len(nums) - 1:
            return jumpTotal

        num = nums[currIdx]
        if num == 0 or num == 1:
            currIdx += 1
            jumpTotal += 1
            continue

        if currIdx + num >= len(nums) - 1:
            return jumpTotal + 1

        maxNumIdx = currIdx + num
        for i in range(currIdx + 1, currIdx + num + 1):
            if i + nums[i] == len(nums) - 1:
                maxNumIdx = i
                break

            if i + nums[i] >= maxNumIdx + nums[maxNumIdx] and i + nums[i] > currIdx + num:
                maxNumIdx = i

        jumpTotal += 1
        currIdx = maxNumIdx

nums = [9,7,9,4,8,1,6,1,5,6,2,1,7,9,0]

print(jump(nums))
