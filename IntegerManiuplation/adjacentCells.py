class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if not cells:
            return []
        #Should repeat every 2 times (8-1) days
        N = (N-1) % 14 + 1
        for day in range(0, N):
            newArrangement = [False]*8
            for i in range(1, len(cells)-1):
                newArrangement[i] = cells[i-1] == cells[i+1]
            cells = newArrangement
            print(cells)
        return [val*1 for val in cells]
 