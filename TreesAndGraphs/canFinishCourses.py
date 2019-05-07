class Solution:   
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.courseMap = {i:{} for i in range(numCourses)}
        self.visit = {i: 0 for i in range(numCourses)}
        for i, j in prerequisites:
            self.courseMap[i][j] = j
        for i in range(numCourses):
            if not self.dfs(i):
                return False

        return True
    def dfs(self, i: int) -> bool:
            
            if self.visit[i] == -1:
                return False
            if self.visit[i] == 1:
                return True
            self.visit[i] = -1
            if(self.courseMap[i] == {}):
                self.visit[i] = 1
                return True
            for j in self.courseMap[i].keys():
                if not self.dfs(self.courseMap[i][j]):
                    return False
            self.visit[i] = 1
            return True