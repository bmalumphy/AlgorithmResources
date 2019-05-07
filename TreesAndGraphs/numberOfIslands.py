class Solution:
    
    def __init__(self):
        self.visited = set()
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        count = 0
        for i in range(0, row):
            for j in range(0, col):
                index = i*col + j
                if not index in self.visited and grid[i][j] == "1": 
                    self.bfs(i,j, grid, row, col)
                    count += 1
        return count
    def bfs(self, i: int, j: int, grid: List[List[str]], row, col):
        queue = [(i,j)]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while queue:
            i, j = queue.pop()
            for dx,dy in directions:
                newX = i+dx
                newY = j+dy
                index = newX*col+newY
                if 0<=newX<row and 0<=newY<col and grid[newX][newY] == "1" and index not in self.visited:
                    self.visited.add(index)
                    queue.insert(0, (newX,newY))
#     def dfsTracker(self, i:int, j:int, visited:List[List[bool]]) -> bool:
#         return i >= 0 and i < self.n and j >= 0 and j < self.m and not visited[i][j] and self.grid[i][j]
        
#     def dfs(self, i: int, j: int, visited: List[List[bool]]):
#         rowTransitions = {0:-1, 
#                           1:-1,
#                           2:-1,
#                           3:0,
#                           4:0,
#                           5:1,
#                           6:1,
#                           7:1
#                          }
#         collumnTransitions = {0:-1, 
#                               1:0,
#                               2:1,
#                               3:-1,
#                               4:1,
#                               5:-1,
#                               6:0,
#                               7:1
#                              }
#         #print(visited)
#         visited[i][j] = True
#         for k in range(0, 8):
#             if self.dfsTracker(i + rowTransitions[k], j + collumnTransitions[k], visited): 
#                 self.dfs(i + rowTransitions[k], j + collumnTransitions[k], visited)
    