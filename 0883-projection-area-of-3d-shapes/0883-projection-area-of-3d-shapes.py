class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        res1=0
        res2=0
        res3=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    res1+=1
        for i in range(len(grid)):
            res2+=max(grid[i])
        for i in range(len(grid[0])):
            m=0
            for j in range(len(grid)):
                if grid[j][i] > m:
                    m=grid[j][i]
            res3+=m
        return res1+res2+res3