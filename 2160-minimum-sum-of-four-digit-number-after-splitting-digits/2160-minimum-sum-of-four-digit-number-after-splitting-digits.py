import numpy as np
class Solution:
    def minimumSum(self, num: int) -> int:
        lis=[int(x) for x in str(num)]
        lis.sort()
        return lis[0]*10+lis[2]+lis[1]*10+lis[3]