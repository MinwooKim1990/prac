import numpy as np
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count=0
        grid1=np.asmatrix(grid)
        grid2=np.asmatrix(grid).T
        for i in range(len(grid)):    
            grid3=len(grid)-np.count_nonzero(np.sum(abs(grid2-np.tile(np.array(grid1)[i], (len(grid),1))),axis=1))
            count+= grid3
        return count
                    