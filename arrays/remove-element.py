# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# This solution does not use pop to improve time complexity - faster than 98% of leetcode submissions
def removeElement(nums, val):
    last = -1
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] != val:
            last = i
            break

    if last == -1:
        return 0

    for i in range(0, last):
        if last <= i:
            return last + 1
        if nums[i] == val:
            nums[i] = nums[last]
            nums[last] = val
            for j in range(last, -1, -1):
                if nums[j] != val:
                    last = j
                    break

    return last + 1

nums = [4, 5]
val = 4

print(removeElement(nums, val))
print(nums)


