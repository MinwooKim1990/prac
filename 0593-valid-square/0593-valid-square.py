import numpy as np
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        pp=[p1,p2,p3,p4]
        res=[]
        if p1==p2==p3==p4:
            return 0
        for i in range(4):
            res.append(sorted([np.dot(np.array(pp[i-3])-np.array(pp[i]),np.array(pp[i-2])-np.array(pp[i])),
                        np.dot(np.array(pp[i-3])-np.array(pp[i]),np.array(pp[i-1])-np.array(pp[i])),
                        np.dot(np.array(pp[i-2])-np.array(pp[i]),np.array(pp[i-1])-np.array(pp[i]))]))
        if res[0][1]==res[0][2]==res[1][1]==res[1][2]==res[2][1]==res[2][2]==res[3][1]==res[3][2]:
            return 1
        return 0