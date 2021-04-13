# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

def removeElement(nums, val):
    ind = len(nums) - 1
    while(ind >= 0):
        if nums[ind] == val:
            nums.pop(ind)
        ind -= 1

    return len(nums)

nums =[0,1,2,2,3,0,4,2]
val = 2

print(removeElement(nums, val))
print(nums)
