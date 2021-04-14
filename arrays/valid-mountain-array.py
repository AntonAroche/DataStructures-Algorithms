# Given an array of integers arr, return true if and only if it is a valid mountain array.
#
# Recall that arr is a mountain array if and only if:
#
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

def validMountainArray(arr):
    size = len(arr)

    if size < 3 or arr[0] >= arr[1]:
        return False

    increasing = True
    for i in range(1, size):
        if arr[i] > arr[i - 1]:
            if not increasing:
                return False
        elif  arr[i] < arr[i - 1]:
            if increasing:
                increasing = False
        else:
            return False

    if arr[size - 1] > arr[size - 2]:
        return False

    return True

arr = [3,5,5]
arr2 = [0,3,2,1]
arr3 = [0,1,2,3,4,5,6,7,8,9]

print(validMountainArray(arr)) # false
print(validMountainArray(arr2)) # true
print(validMountainArray(arr3)) # false
