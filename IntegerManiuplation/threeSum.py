class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []
        
        #First sort the array so our pointers can easily keep track of position
        #O(n*log(n))
        nums.sort()
        
        #returns empty of all numbers are positive or negative besides 0
        solutions = []

        if nums[0] > 0:
            return []
        if nums[-1] < 0:
            return []
        if len(nums) == 3 and sum(nums) == 0:
            solutions.append(nums)
            return solutions
        elif len(nums) <= 3:
            return []
        #initialize our pointers and solution
        n = len(nums)
        
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if(nums[i] > 0):
                return solutions
            l, r = i+1, n-1

            while l<r:
                x = nums[i]
                y = nums[l]
                z = nums[r]
                if x + y + z > 0:
                    r -=1
                elif x +y + z < 0:
                    l += 1
                else:
                    solutions.append([x, y, z])
                    while l < r and y == nums[l+1]:
                        l += 1
                    while l < r and z == nums[r-1]:
                        r -=1
                    l+=1
                    r-=1

        return solutions
                
