import numpy as np

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        pp = [p1, p2, p3, p4]
        res = []
        if p1 == p2 == p3 == p4:
            return False
        
        dot_products = [[np.dot(np.array(pp[i-3])-np.array(pp[i]),np.array(pp[i-2])-np.array(pp[i])),
                        np.dot(np.array(pp[i-3])-np.array(pp[i]),np.array(pp[i-1])-np.array(pp[i])),
                        np.dot(np.array(pp[i-2])-np.array(pp[i]),np.array(pp[i-1])-np.array(pp[i]))] for i in range(2)]
        
        for i in range(2):
            res.append(sorted(dot_products[i]))
            
        if res[0][1]==res[0][2]==res[1][1]==res[1][2]:
            return True
        
        return False
