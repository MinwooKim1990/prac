import numpy as np
class Solution:
    def scoreOfString(self, s: str) -> int:
        tot = 0
        for i in range(len(s)-1):
            tot+=abs(ord(s[i])-ord(s[i+1]))
        return tot