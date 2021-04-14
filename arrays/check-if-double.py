# Given an array arr of integers, check if there exists two integers N and M
# such that N is the double of M ( i.e. N = 2 * M).

def checkIfExist(arr):
    dict = {}
    for i in range(0, len(arr)):
        curr = arr[i]
        if (curr * 2 in dict) or (curr / 2 in dict):
            return True;

        dict[curr] = i

    return False

arr = [3, 1, 7, 11]
arr2 = [7, 1, 14, 11]
print(checkIfExist(arr)) # false
print(checkIfExist(arr2)) # true
