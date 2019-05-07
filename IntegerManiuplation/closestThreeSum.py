import sys

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums:
            return []
        
        #First sort the array so our pointers can easily keep track of position
        #O(n*log(n))
        nums.sort()
        
        #returns empty of all numbers are positive or negative besides 0
        solution = sys.maxsize
        n = len(nums)
        if n == 3:
            return sum(nums)        
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1

            while l<r:
                x = nums[i]
                y = nums[l]
                z = nums[r]
                if x + y + z > target:
                    if abs(x + y + z - target) < abs(target - solution):
                        solution = x + y + z
                    r -=1
                elif x + y + z < target:
                    if abs(target - x - y - z) < abs(target - solution):
                        solution = x + y + z
                    l += 1
                else:
                    return target
            
        return solution