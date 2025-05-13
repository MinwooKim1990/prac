import numpy as np
class Solution:
    def scoreOfString(self, s: str) -> int:
        return int(sum([abs(c) for c in np.array([ord(a) for a in s[:-1]])-np.array([ord(b) for b in s[1:]])]))