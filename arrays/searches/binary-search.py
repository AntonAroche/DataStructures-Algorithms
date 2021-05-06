# Given a sorted array of elements and an integer n, a binary search
# will return the index of the value with O(log n) time complexity.
# Returns -1 if the element is not found.
# Author: Anton Aroche

def binarySearch(arr, n):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == n:
            return mid
        elif arr[mid] > n:
            right = mid - 1
        else:
            left = mid + 1

    return -1

def binarySearchRecursive(arr, left, right, n):
    mid = (left + right) // 2

    if arr[mid] == n:
        return mid
    elif left > right:
        return -1
    elif arr[mid] > n:
        return binarySearchRecursive(arr, left, mid - 1, n)
    else:
        return binarySearchRecursive(arr, mid + 1, right, n)

nums = [ 2, 3, 4, 10, 40 ]
n = 10

print(binarySearch(nums, n)) # Will return 3
print(binarySearchRecursive(nums, 0, len(nums) - 1, n)) # Will return 3

