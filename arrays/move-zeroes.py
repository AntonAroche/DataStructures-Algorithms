# Given an integer array nums, move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.

def moveZeroes(nums):
    currMove = -1
    for i in range(0, len(nums)):
        if nums[i] != 0:
            if currMove == -1:
                continue
            nums[currMove] = nums[i]
            nums[i] = 0
            currMove += 1
        else:
            # Initializes currmove to the first zero
            if currMove == -1:
                currMove = i
    return nums


nums =  [1,0,1]

print(moveZeroes(nums))
