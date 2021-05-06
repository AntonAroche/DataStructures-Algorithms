# Bubble Sort works by iterating through an array and swapping adjacent elements if they
# are out of order, until no swap is detected. Its worst case execution time is O(n^2), but
# it has a best case execution time of O(n). Its space complexity is only O(1).

def bubbleSort(arr):
    sorting = True

    while sorting:
        sorting = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                curr = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = curr
                sorting = True

    return arr

nums = [64,15,12,22,11]

print(bubbleSort(nums))
