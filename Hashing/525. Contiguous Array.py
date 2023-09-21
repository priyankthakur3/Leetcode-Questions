# class Solution:
#     def findMaxLength(self, nums: List[int]) -> int:
#         maxLen = 0
#         sum = 0
#         hashMap = {0:-1}
#         for i in range(len(nums)):
#             if nums[i]==0:
#                 sum -= 1
#             if nums[i]==1:
#                 sum += 1

#             if sum in hashMap:
#                 maxLen = max(maxLen,i-hashMap[sum])
#             else:
#                 hashMap[sum] = i
#         return maxLen


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLen = 0
        sum = 0
        hashMap = {0: -1}
        for i in range(len(nums)):
            if nums[i] == 0:
                sum -= 1
            if nums[i] == 1:
                sum += 1

            if(sum in hashMap):
                maxLen = max(maxLen, i - hashMap[sum])
            else:
                hashMap[sum] = i
        return maxLen
