class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # get max number of bananas
        left, right = 1, max(piles)
        # initialize res to right for max amount of bananas
        res = right
        while left <= right:
            mid = left + (right - left)// 2
            hours = 0
            # get count of hours to consume all bananas
            for p in piles:
                hours += math.ceil(p / mid)
            # if calculated hours is less than or equal to h
            # and reduce range to left side
            if hours <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res
