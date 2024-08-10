class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort all intervals on start value
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]] # edge case if intervals is of length 1
        for start,end in intervals[1:]:
            # check if current intervals start is less than or last intervals end
            # if current interval lies within or is extending it
            if start <= output[-1][1]: 
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start,end])
            
        return output