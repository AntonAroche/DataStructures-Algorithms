# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has a size equal to m + n such that it has enough
# space to hold additional elements from nums2.

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

def merge(nums1, m, nums2, n):
    size = m + n
    n1 = 0;
    n2 = 0;

    for i in range(0, size):
        fits = nums1[n1] <= nums2[n2] and nums1[n1 + 1] >= nums2[n2]
        if fits or n1 == m - 1:
            nums1.pop(size - 1)
            nums1.insert(i + 1, nums2[n2])
            if (n2 < n - 1):
                n2 += 1
            else:
                break
        else:
            n1 += 1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)

print(nums1)

