# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

def removeDuplicates(nums):
    size = len(nums)
    idx = 0
    while (idx < size - 1):
        if nums[idx] == nums[idx + 1]:
            nums.pop(idx)
            size -= 1
        else:
            idx += 1
    return len(nums)


nums = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))
