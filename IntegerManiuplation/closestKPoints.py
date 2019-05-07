class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        solution = []
        
        #two simplest edge cases
        if not points:
            return solution
        if len(points) == K:
            return points
        points.sort(key = lambda l: l[0]**2+l[1]**2)
        for i in range(0,K):
            solution.append(points[i])
        return solution