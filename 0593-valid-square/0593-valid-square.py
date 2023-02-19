import numpy as np

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        pp = [np.array(p1), np.array(p2), np.array(p3), np.array(p4)]
        res = []
        if p1 == p2 == p3 == p4:
            return False
        
        dot_products = [[np.dot(pp[i-3]-pp[i],pp[i-2]-pp[i]),
                        np.dot(pp[i-3]-pp[i],pp[i-1]-pp[i]),
                        np.dot(pp[i-2]-pp[i],pp[i-1]-pp[i])] for i in range(2)]
        
        for i in range(2):
            res.append(sorted(dot_products[i]))
            
        if res[0][1]==res[0][2]==res[1][1]==res[1][2]:
            return True
        
        return False
