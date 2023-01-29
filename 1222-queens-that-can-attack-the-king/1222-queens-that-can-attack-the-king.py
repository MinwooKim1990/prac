import numpy as np
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        """def po(a):
            dire={}
            temp=[]
            b=np.array(a)
            while b[1] != 0:
                b=b+[0,-1]
                temp.append(list(b))
                b=np.array(b)
            dire['u']=temp
            temp=[]
            b=np.array(a)
            while b[0] != 8 and b[1] != 0:
                b=b+[1,-1]
                temp.append(list(b))
                b=np.array(b)
            dire['ur']=temp
            temp=[]
            b=np.array(a)
            while b[0] != 8:
                b=b+[1,0]
                temp.append(list(b))
                b=np.array(b)
            dire['r']=temp
            temp=[]
            b=np.array(a)
            while b[0] != 8 and b[1] != 8:
                b=b+[1,1]
                temp.append(list(b))
                b=np.array(b)
            dire['dr']=temp
            temp=[]
            b=np.array(a)
            while b[1] != 8:
                b=b+[0,1]
                temp.append(list(b))
                b=np.array(b)
            dire['d']=temp
            temp=[]
            b=np.array(a)
            while b[0] != 0 and b[1] != 8:
                b=b+[-1,1]
                temp.append(list(b))
                b=np.array(b)
            dire['dl']=temp
            temp=[]
            b=np.array(a)
            while b[0] != 0:
                b=b+[-1,0]
                temp.append(list(b))
                b=np.array(b)
            dire['l']=temp
            temp=[]
            b=np.array(a)
            while b[0] != 0 and b[1] != 0:
                b=b+[-1,-1]
                temp.append(list(b))
                b=np.array(b)
            dire['ul']=temp
            temp=[]
            return dire"""
        res = []
        queens = {(i, j) for i, j in queens}
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in range(1, 8):
                    x, y = king[0] + i * k, king[1] + j * k
                    if (x, y) in queens:
                        res.append([x, y])
                        break
        return res
