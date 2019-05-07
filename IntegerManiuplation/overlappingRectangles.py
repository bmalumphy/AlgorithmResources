class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return self.doesIntersect((rec1[0], rec1[2]), (rec2[0], rec2[2])) and self.doesIntersect((rec1[1], rec1[3]), (rec2[1], rec2[3]))
    
    def doesIntersect(self, a: tuple, b: tuple):
        return max(0, min(a[1], b[1]) - max(a[0], b[0])) > 0