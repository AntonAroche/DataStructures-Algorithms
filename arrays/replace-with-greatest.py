# Given an array arr, replace every element in that array with the
# greatest element among the elements to its right, and replace the last element with -1.
#
# After doing so, return the array.

def replaceElements(arr):
    currIdx = 0
    for i in range(0, len(arr) - 1):
        if i < currIdx:
            arr[i] = arr[currIdx]
            continue

        currIdx = i + 1

        for j in range(i + 1, len(arr)):
            if arr[j] > arr[currIdx]:
                currIdx = j

        arr[i] = arr[currIdx]

    arr[len(arr) - 1] = -1
    return arr

arr = [17,18,5,4,6,1]
print (replaceElements(arr))
