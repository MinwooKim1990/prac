import numpy as np
class Solution:
    def minimumSum(self, num: int) -> int:
        lis=[int(x) for x in str(num)]
        lis.sort()
        mini1=lis[0]
        mini2=lis[1]
        nex=lis[2]
        nex2=lis[3]
        return mini1*10+nex+mini2*10+nex2