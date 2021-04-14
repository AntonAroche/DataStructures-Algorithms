# Given an array A of non-negative integers, return an array consisting of all the
# even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.

# This solution uses in-place modification for ideal space complexity.
def sortArrayByParity(A):
    even = -1
    for i in range(len(A) - 1, -1, -1):
        if A[i] % 2 == 0:
            even = i
            break

    for i in range(0, len(A)):
        if A[i] % 2 != 0:
            if i > even:
                return A

            curr = A[i]
            A[i] = A[even]
            A[even] = curr

            for j in range(even, -1, -1):
                if A[j] % 2 == 0:
                    if j <= i:
                        return A
                    even = j
                    break

    return A

# This solution achieves O(n) time complexity by storing elements in arrays.
def sortArrayByParityFast(A):
    even = []
    odd = []

    for n in A:
         if n % 2 == 0:
             even.append(n)
         else:
            odd.append(n)

    return even + odd

nums = [3,1,2,4]
print(sortArrayByParityFast(nums))



