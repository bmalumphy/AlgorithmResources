import collections, heapq

class Solution:
    """
    I am going to investigate the heck out of graph stuff now. I was
    completely unprepared for this question. Below is the recommended
    approach from the article. I mainly copied it here so I could have it
    as a reference. I did not solve this problem myself.
    
    I WILL get to where I can do these though.
    """
    def cutOffTree(self, forest: List[List[int]]) -> int:
        trees = sorted((v, r, c) for r, row in enumerate(forest)
                       for c, v in enumerate(row) if v > 1)
        sr = sc = ans = 0
        for _, tr, tc in trees:
            d = self.hadlocks(forest, sr, sc, tr, tc)
            if d < 0: return -1
            ans += d
            sr, sc = tr, tc
        return ans
    
    def bfs(self, forest, sr, sc, tr, tc):
        R, C = len(forest), len(forest[0])
        queue = collections.deque([(sr, sc, 0)])
        seen = {(sr, sc)}
        while queue:
            r, c, d = queue.popleft()
            if r == tr and c == tc:
                return d
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if (0 <= nr < R and 0 <= nc < C and
                        (nr, nc) not in seen and forest[nr][nc]):
                    seen.add((nr, nc))
                    queue.append((nr, nc, d+1))
        return -1 
    
    def astar(self, forest, sr, sc, tr, tc):
        R, C = len(forest), len(forest[0])
        heap = [(0, 0, sr, sc)]
        cost = {(sr, sc): 0}
        while heap:
            f, g, r, c = heapq.heappop(heap)
            if r == tr and c == tc: return g
            for nr, nc in ((r-1,c), (r+1,c), (r,c-1), (r,c+1)):
                if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:
                    ncost = g + 1 + abs(nr - tr) + abs(nc - tc)
                    if ncost < cost.get((nr, nc), 9999):
                        cost[nr, nc] = ncost
                        heapq.heappush(heap, (ncost, g+1, nr, nc))
        return -1
    
    def hadlocks(self, forest, sr, sc, tr, tc):
        R, C = len(forest), len(forest[0])
        processed = set()
        deque = collections.deque([(0, sr, sc)])
        while deque:
            detours, r, c = deque.popleft()
            if (r, c) not in processed:
                processed.add((r, c))
                if r == tr and c == tc:
                    return abs(sr-tr) + abs(sc-tc) + 2*detours
                for nr, nc, closer in ((r-1, c, r > tr), (r+1, c, r < tr),
                                       (r, c-1, c > tc), (r, c+1, c < tc)):
                    if 0 <= nr < R and 0 <= nc < C and forest[nr][nc]:
                        if closer:
                            deque.appendleft((detours, nr, nc))
                        else:
                            deque.append((detours+1, nr, nc))
        return -1