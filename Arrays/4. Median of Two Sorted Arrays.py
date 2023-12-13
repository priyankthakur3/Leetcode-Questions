class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        l1 , l2 = len(nums1), len(nums2)
        mid = (l1 + l2) / 2 
        i , j = 0 , 0
        while len(result) <= mid:
            if i == len(nums1):
                result.append(nums2[j])
                j += 1
            elif j == len(nums2):
                result.append(nums1[i])
                i += 1

            elif nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        if (l1 + l2) % 2 == 0:
            return (result[len(result) - 1] + result[len(result) - 2]) / 2
        else:
            return result[-1]
            