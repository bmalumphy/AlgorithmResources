import functools

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda l:l[0])
        
        solution = []
        if not intervals:
            return solution
        mini, maxi = intervals[0]
        for l, r in intervals:
            if l > maxi:
                solution.append([mini, maxi])
                mini = l
                maxi = r
            else:
                maxi = max(maxi, r)
        solution.append([mini, maxi])
        return solution