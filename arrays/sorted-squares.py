# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

def sortedSquaresEasy(nums):
    return sorted(i ** 2 for i in nums)

def sortedSquares(nums):
    size = len(nums)
    new = []
    left = 0
    right = size - 1

    for i in range(0, size):
        if abs(nums[left]) > abs(nums[right]):
            new.insert(0, nums[left] ** 2)
            left = left + 1
        else:
            new.insert(0, nums[right] ** 2)
            right = right - 1

    return new

nums = [-4,-2,-1,0,1,3,10]

print(sortedSquaresEasy(nums))
print(sortedSquares(nums))

