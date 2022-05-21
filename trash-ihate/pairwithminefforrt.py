 from typing import List
 class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
    	# Copy pasta
    	h = [(0,0,0)]
        row, col = len(heights), len(heights[0])
        visited = set()
        while h:
            d,r,c = heappop(h)
            if (r,c) in visited: continue
            if (r,c) == (row-1,col-1):
                return d
            visited.add((r,c))
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                if 0 <= r + dr < row and 0 <= c + dc < col:
                    jump = abs(heights[r][c]-heights[r+dr][c+dc])
                    heappush(h, (max(d,jump), r+dr, c+dc))