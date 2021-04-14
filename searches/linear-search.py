# Given an array of elements, a linear search will go through each element in an array
# sequentially to find a match, and returns its index.
# The search makes no assumptions on whether the array is sorted.

# Author: Anton Aroche

def linearSearch(arr, n):
    for i in range(0, len(arr)):
        if arr[i] == n:
            return i


nums = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]

print(linearSearch(nums, 50)) # will return 5

