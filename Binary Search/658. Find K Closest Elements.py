class Solution(object):
    def findClosestElements(self, arr, k, x):
        lo, hi = 0, len(arr)-k
        while lo < hi:
            mid = (lo + hi)//2
            #  x - arr[mid] > arr[mid + k] - x in the code is used to 
            # determine whether the element at the current mid index 
            # is farther away from x than the element at mid + k 
            # (the last element of the current window of k elements
            if x-arr[mid] > arr[mid+k]-x:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo:lo+k]