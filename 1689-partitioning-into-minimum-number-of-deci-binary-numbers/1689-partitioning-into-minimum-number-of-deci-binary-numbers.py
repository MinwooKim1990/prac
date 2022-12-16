import numpy as np
class Solution:
    def minPartitions(self, n: str) -> int:
        a=list(n)
        for i in range(len(a)):
            a[i]=int(a[i])
        return np.max(a)