# The selection sort algoritm sorts an array by finding each minimum element and placing it
# in order. It is a fairly slow algoritm with O(n^2) time complexity, but it has
# a space complexity of only O(1).

def selectionSort(arr):
    for i in range(len(arr)):
        minIdx = i
        curr = arr[i]
        for j in range(i + 1, len(arr)):
            if (arr[j] < curr):
                minIdx = j

        arr[i] = arr[minIdx]
        arr[minIdx] = curr

    return arr

nums = [64,15,12,22,11]

print(selectionSort(nums))
