import numpy as np
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        l=len(satisfaction)
        satisfaction.sort()
        sco=[]
        for i in range(l):
            b=np.array(range(1,l+1-i))
            sco.append(sum(satisfaction*b))
            del satisfaction[0]
        msco=np.max(sco)
        if msco <= 0 :
            return 0
        else:
            return msco